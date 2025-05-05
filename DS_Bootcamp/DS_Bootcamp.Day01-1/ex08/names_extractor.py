import sys


def prepare_data_to_tsv(rel_path: str) -> list:
    out: list = []
    with open(rel_path, "r") as file:
        out.append("Name\tSurname\tE-mail\n")
        for line in file:
            name_and_surname, _ = line.split("@")
            name, surname = name_and_surname.split('.')
            out.append(f"{name.capitalize()}\t{surname.capitalize()}\t{line}")
    return out


def write_tsv(my_list: list, tsv_name: str) -> None:
    with open(tsv_name, "w") as file:
        for line in my_list:
            file.write(line)


def argv_check(my_argv: list) -> str:
    if len(my_argv) != 2:
        # if there are no arguments or too many arguments, the program displays nothing
        return ""

    argv: list = sys.argv[1].split(",")
    argv = [value.strip() for value in argv]

    if len(argv) != 1:
        # if there are more than 1 path
        return ""

    return my_argv[1]


def main() -> None:
    try:
        argv_checked: str = argv_check(sys.argv)
        to_tsv: list = prepare_data_to_tsv(argv_checked)
        write_tsv(to_tsv, "employees.tsv")

    except FileNotFoundError as error:
        print("Wrong path name or more than one path or no such file in dir")


if __name__ == '__main__':
    main()
