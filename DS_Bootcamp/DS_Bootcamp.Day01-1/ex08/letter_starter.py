import sys


def create_frst_prgrph(rel_path: str, email_argv: str) -> str:
    out: dict = {}
    with open(rel_path, "r") as file:
        for line in file:
            name, surname, email_from_table = line.replace("\n","").split("\t")
            if email_from_table not in out:
                out[email_from_table] = name

    return (f"Dear {out[email_argv]}, welcome to our team. We are sure that it will be a pleasure to work with"
            f"you. That’s a precondition for the professionals that our company hires.")


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
        msg: str = create_frst_prgrph("employees.tsv", argv_checked)
        print(msg)

    except KeyError as error:
        print("Wrong email name or more than one email")

    except FileNotFoundError as error:
        print("No employees.tsv in dir")


if __name__ == '__main__':
    main()
