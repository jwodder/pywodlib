"""
Synchronized queues (both FIFO and LIFO) for use by a collection of concurrent
workers that are both producers and consumers.  Specifically, after the queue
is initialized with some starting tasks, each worker iterates through the queue
task by task as available; for each task, the worker operating on it adds some
number of new tasks to the queue and then marks the current task finished.
Once the queue is empty and all tasks have been marked finished, the iterators
stop yielding values.

Sample usage by a worker:

.. code:: python

    for taskctx in job_queue:
        with taskctx as task:
            # Operate on task
            # Call job_queue.put(new_task) some number of times

Based on <https://gist.github.com/jart/0a71cde3ca7261f77080a3625a21672b>
"""

from abc import ABC, abstractmethod
from collections import deque
from contextlib import contextmanager
from threading import Condition, Lock
from typing import ContextManager, Deque, Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


class AbstractJobQueue(ABC, Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
        self._lock = Lock()
        self._cond = Condition(self._lock)
        self._queue: Deque[T] = deque()
        self._tasks = 0
        if iterable is not None:
            self._queue.extend(iterable)
            self._tasks += len(self._queue)

    @abstractmethod
    def _get(self) -> T:
        ...

    def __iter__(self) -> Iterable[ContextManager[T]]:
        while True:
            with self._lock:
                while True:
                    if not self._tasks:
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
                self._tasks -= 1
                if self._tasks <= 0:
                    self._cond.notify_all()

    def put(self, value: T) -> None:
        with self._lock:
            self._queue.append(value)
            self._tasks += 1
            self._cond.notify()


class JobQueue(AbstractJobQueue[T]):
    def _get(self) -> T:
        return self._queue.popleft()


class JobStack(AbstractJobQueue[T]):
    def _get(self) -> T:
        return self._queue.pop()
