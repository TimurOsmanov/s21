import sys


class Research:
    def __init__(self) -> None:
        try:
            self.path: str = sys.argv[1]
        except IndexError:
            self.path = ''

    def file_reader(self, has_header: bool = True) -> list:
        out: list = []
        try:
            with open(self.path, "r") as file:
                lines_count: int = 0
                counter: int = 0 if has_header else -1
                for num, line in enumerate(file.read().split("\n")):
                    head,tail = line.split(",")
                    if num != counter:
                        if int(head) + int(tail) != 1:
                            out = ["ValueError: wrong structure/data"]
                            break
                        out.append([int(head), int(tail)])
                        lines_count += 1

            if lines_count < 1:
                out = [f"ValueError: wrong structure/data"]
        except FileNotFoundError as error:
            out = [f"FileNotFoundError: {error} No such file"]
        except ValueError as error:
            out = [f"ValueError: {error} wrong structure/data"]

        return out

    class Calculations:
        @staticmethod
        def count(data: list) -> tuple[int, int]:
            head_sum: int = 0; tail_sum: int = 0
            for pair in data:
                head_sum += pair[0]
                tail_sum += pair[1]
            return head_sum, tail_sum

        @staticmethod
        def fractions(pair: tuple) -> tuple[float, float]:
            return pair[0]/sum(pair), 1 - pair[0]/sum(pair)


def main() -> None:
    try:
        data: list = Research().file_reader()
        print(data)
        count: tuple = Research().Calculations.count(data)
        print(*count)
        fractions: tuple = Research().Calculations.fractions(count)
        print(*fractions)
    except TypeError:
        pass


if __name__ == '__main__':
    main()
