#!/usr/bin/env python3
import timeit
import random
from collections import Counter


def my_func(arr: list) -> dict:
    counts: list = [0] * 101
    for val in arr:
        counts[val] += 1
    return {num: val for num, val in enumerate(counts)}


def my_top10(arr: list) -> list:
    my_dict: dict = my_func(arr)
    out: list = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
    return out[:10]


def counter_(arr: list) -> dict:
    return dict(Counter(arr))


def counter_top10(arr: list) -> list:
    return Counter(arr).most_common(10)


def main() -> str:
    out: str = ''
    arr = [random.randint(0, 100) for _ in range(1_000_000)]

    times: dict = {"my function": timeit.timeit(f'my_func({arr})', number=1, globals=globals()),
           "Counter": timeit.timeit(f'counter_({arr})', number=1, globals=globals()),
           "my top": timeit.timeit(f'my_top10({arr})', number=1, globals=globals()),
           "Counter's top": timeit.timeit(f'counter_top10({arr})', number=1, globals=globals()),}

    for func in times:
        out += f"{func}: {times[func]:.7f}" + '\n'

    return out[:-1]


if __name__ == "__main__":
    print(main())
