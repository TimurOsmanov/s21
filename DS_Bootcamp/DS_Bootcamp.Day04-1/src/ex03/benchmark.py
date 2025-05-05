#!/usr/bin/env python3
import timeit
import sys
from functools import reduce


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 4:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, func_name, num, sum_num = my_argv
    return func_name, num, sum_num


def loop(sum_num: int) -> int:
    sum_: int = 0
    for i in range(1, sum_num + 1):
        sum_ += i * i
    return sum_


def reduce_(sum_num: int):
    return reduce(lambda x, y: x + y * y, range(1, sum_num + 1))


def main() -> str:
    try:
        func_name, num, sum_num = argv_check(sys.argv)
        num = int(num); sum_num = int(sum_num)
        times: dict = {'loop': 'loop', 'reduce': 'reduce_'}
        return str(timeit.timeit(f'{times[func_name]}({sum_num})', number=num, globals=globals()))

    except ValueError:
        return "ValueError: wrong args/num isn't int"
    except KeyError:
        return "KeyError: wrong func name"


if __name__ == "__main__":
    print(main())
