import time

def itersleep(interval, maxtime=None, yield_first=False):
    if yield_first:
        yield
    if maxtime is None:
        while True:
            ### Subtract the time since the last `yield` from `interval`???
            time.sleep(interval)
            yield
    else:
        gettime = getattr(time, 'monotonic', time.time)
        end_time = gettime() + maxtime
        while True:
            time_left = end_time - gettime()
            if time_left <= 0:
                return
            ### Subtract the time since the last `yield` from `interval`???
            time.sleep(min(interval, time_left))
            yield

def itersleep_exponential(base: float = 2, multiplier: float = 1, qty: Optional[int] = None) -> Iterator[None]:
    n = 0
    while qty is None or n < qty:
        time.sleep(base ** n * multiplier)
        yield
        n += 1
