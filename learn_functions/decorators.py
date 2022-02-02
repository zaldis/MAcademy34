import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Duration of {func.__name__} is {end-start} seconds')
        return result
    return wrapper


@timing
def range_sum(end: int) -> int:
    """
    end = 10
    sm = 0 + 1 + 2 + 3 + .. 9
    """
    step = 1 if end > 0 else -1
    start = 0

    sm = 0
    while start != end:
        start += step
        sm += start
    return sm
# range_sum = timing(range_sum)


@timing
def range_sum_progress(end: int) -> int:
    step = 1 if end > 0 else -1
    a1 = 0
    a2 = end - step
    cnt = abs(end)

    sm = (a1 + a2) * cnt // 2
    return sm
# range_sum_progress = timing(range_sum_progress)


range_sum(10_000_000)
range_sum_progress(10_000_000)

# start = time.time()
# range_sum(10_000_000)
# end = time.time()
# print(f'Duration 1 is {end-start} seconds')


# start = time.time()
# range_sum_progress(10_000_000)
# end = time.time()
# print(f'Duration 2 is {end-start} seconds')