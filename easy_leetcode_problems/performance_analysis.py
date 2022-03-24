from functools import wraps
from memory_profiler import memory_usage
from pprint import pprint
from time import time
from typing import Callable, Tuple, TypeVar


ONE_TENTHS_SECOND = 0.1
QUARTER_SECOND = 0.25
HALF_SECOND = 0.5
ONE_SECOND = 1
return_type = TypeVar("return_type")


def time_algorithm(f: Callable,
                   n_runs: int,
                   *args,
                   **kw) -> Tuple[return_type, float]:
    time_start: float = time()
    for _ in range(n_runs):
        result: Tuple[return_type, float] = f(*args, **kw)
    time_end: float = time()
    total_time = time_end - time_start
    return (result, total_time)


def determine_n_runs(time: float) -> int:
    if time <= ONE_TENTHS_SECOND:
        return 10_000
    elif time <= QUARTER_SECOND:
        return 1_000
    elif time <= HALF_SECOND:
        return 100
    else:
        return 1


def measure_performance_x_runs(f):
    """Performance decorator to measure the time required to run
    the function x times with identical inputs, and the memory
    required for a single run."""
    @wraps(f)
    def wrap(*args, **kw):
        # measure one run's max memory intake
        mem = memory_usage(proc=(f, args, kw), max_usage=True)
        # measure the time on a single run to determine the n of iterations
        result, time = time_algorithm(f, 1, *args, **kw)
        n_runs = determine_n_runs(time)
        # apply iterations to better compare negligible runtime differences
        _, time = time_algorithm(f, n_runs, *args, **kw)
        print(f"{f.__name__} with args = ")
        if isinstance(vars(args[0]), dict):
            for k, v in vars(args[0]).items():
                pprint(f"{k}:{vars(v)}")
        else:
            pprint(vars(args[0]))
        print(f"Total time for {n_runs} run(s): {time}")
        print(f"Total memory for one run: {mem}\n")
        return result
    return wrap
