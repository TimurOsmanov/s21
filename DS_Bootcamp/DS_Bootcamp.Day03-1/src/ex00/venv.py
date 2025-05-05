#!/usr/bin/env python3
import os

# python3 -m venv shireeth
# source shireeth/bin/activate
# source ../ex00/shireeth/bin/activate
# deactivate

def print_venv() -> None:
    my_env = os.environ["VIRTUAL_ENV"]
    print(f"Your current virtual env is {my_env}")


if __name__ == "__main__":
    print_venv()
