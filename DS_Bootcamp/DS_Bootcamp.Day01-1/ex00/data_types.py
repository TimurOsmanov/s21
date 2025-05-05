def main() -> None:
    my_int: int = 0
    my_str: str = ''
    my_float: float = 0.0
    my_bool: bool = True
    my_list: list = list()
    my_dict: dict = dict()
    my_tuple: tuple = tuple()
    my_set: set = set()

    output: list = list()

    for my_type in my_int, my_str, my_float, my_bool, my_list, my_dict, my_tuple, my_set:
        temp_str: str = str(type(my_type))
        output.append(temp_str.split("'")[1])

    print("[", end='')
    print(*output, sep=', ', end='')
    print("]")

if __name__ == '__main__':
      main()
