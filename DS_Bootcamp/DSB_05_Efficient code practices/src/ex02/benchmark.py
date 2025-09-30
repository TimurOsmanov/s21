#!/usr/bin/env python3
import timeit
import sys


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 3:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, func_name, num = my_argv
    return func_name, num


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


def filter_(emails_list: list) -> filter:
    return filter(lambda email: 'gmail.com' in email,
                  emails_list)


def main() -> str:
    emails: list = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    try:
        func_name, num = argv_check(sys.argv)
        num = int(num)
        times: dict = {'loop': 'loop', 'list_comprehension': 'list_comprehension', 'map': 'map_', 'filter': 'filter_',}
        return str(timeit.timeit(f'{times[func_name]}({emails*5})', number=num, globals=globals()))

    except ValueError:
        return "ValueError: wrong args/num isn't int"
    except KeyError:
        return "KeyError: wrong func name"


if __name__ == "__main__":
    print(main())
