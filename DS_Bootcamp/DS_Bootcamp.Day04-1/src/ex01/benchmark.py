#!/usr/bin/env python3
import timeit


def loop(emails_list: list) -> list:
    out: list = []
    for email in emails_list:
        if 'gmail.com' in email:
            out.append(email)
    return out


def list_comprehension(emails_list: list) -> list:
    return [email for email in emails_list if 'gmail.com' in email]


def map_(emails_list: list) -> map:
    return map(lambda email: 'gmail.com' in email,
                    emails_list)


def main() -> str:
    emails: list = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    num: int = 90_000_000

    times: dict = {
        'loop': (timeit.timeit(f'loop({emails*5})', number=num, globals=globals()),
                 "it is better to use a loop"),
        'list_comprehension': (timeit.timeit(f'list_comprehension({emails*5})', number=num, globals=globals()),
                                "it is better to use a list comprehension"),
        'map_': (timeit.timeit(f'map_({emails * 5})', number=num, globals=globals()),
                 "it is better to use a map")
    }
    out: list = sorted(times, key=lambda x: times[x][0])

    return f'{times[out[0]][1]}\n{times[out[0]][0]} vs {times[out[1]][0]} vs {times[out[2]][0]}'


if __name__ == "__main__":
    print(main())
