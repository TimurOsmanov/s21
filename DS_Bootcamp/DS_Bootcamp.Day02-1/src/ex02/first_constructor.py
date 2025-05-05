import sys


class Research:
    def __init__(self) -> None:
        try:
            self.path = sys.argv[1]
        except IndexError:
            self.path = ''

    def file_reader(self) -> str:
        out: str = ""
        try:
            with open(self.path, "r") as file:
                lines_count = 0
                for num, line in enumerate(file.read().split("\n")):
                    out += line + '\n'
                    head,tail = line.split(",")
                    if num != 0:
                        if int(head) + int(tail) != 1:
                            out = "ValueError: wrong structure/data "
                            break
                        lines_count += 1
            if lines_count < 1:
                out = f"ValueError: wrong structure/data "
        except FileNotFoundError as error:
            out = f"FileNotFoundError: {error} No such file "
        except ValueError as error:
            out = f"ValueError: {error} wrong structure/data "

        return out[:-1]


if __name__ == '__main__':
    print(Research().file_reader())
