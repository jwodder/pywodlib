"""
Synchronized queues (both FIFO and LIFO) for use by a collection of concurrent
workers that are both producers and consumers.  Specifically, after the queue
is initialized with some starting jobs, each worker iterates through the queue
job by job as available; for each job, the worker operating on it adds some
number of new jobs to the queue and then marks the current job finished.  Once
the queue is empty and all jobs have been marked finished, the iterators stop
yielding values.

Sample usage by a worker:

.. code:: python

    for jobctx in job_queue:
        with jobctx as job:
            # Operate on job
            # Call job_queue.put(new_job) some number of times

Based on <https://gist.github.com/jart/0a71cde3ca7261f77080a3625a21672b>
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterable, Iterator
from contextlib import AbstractContextManager, contextmanager
from threading import Condition, Lock
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class AbstractJobQueue(ABC, Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
        self._lock = Lock()
        self._cond = Condition(self._lock)
        self._queue: deque[T] = deque()
        self._jobs = 0
        if iterable is not None:
            self._queue.extend(iterable)
            self._jobs += len(self._queue)

    @abstractmethod
    def _get(self) -> T:
        ...

    def __iter__(self) -> Iterator[AbstractContextManager[T]]:
        while True:
            with self._lock:
                while True:
                    if not self._jobs:
                        return
                    if not self._queue:
                        self._cond.wait()
                        continue
                    value = self._get()
                    break
            yield self._job_ctx(value)

    @contextmanager
    def _job_ctx(self, value: T) -> Iterator[T]:
        try:
            yield value
        finally:
            with self._lock:
                self._jobs -= 1
                if self._jobs <= 0:
                    self._cond.notify_all()

    def put(self, value: T) -> None:
        with self._lock:
            self._queue.append(value)
            self._jobs += 1
            self._cond.notify()


class JobQueue(AbstractJobQueue[T]):
    def _get(self) -> T:
        return self._queue.popleft()


class JobStack(AbstractJobQueue[T]):
    def _get(self) -> T:
        return self._queue.pop()
