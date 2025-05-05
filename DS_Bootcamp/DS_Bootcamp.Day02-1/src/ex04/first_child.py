import sys
from random import randint


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
        def __init__(self, data) -> None:
            self.data = data

        def count(self) -> tuple[int, int]:
            head_sum: int = 0; tail_sum: int = 0
            for pair in self.data:
                head_sum += pair[0]
                tail_sum += pair[1]
            return head_sum, tail_sum

        @staticmethod
        def fractions(pair: tuple) -> tuple[float, float]:
            return pair[0]/sum(pair), 1 - pair[0]/sum(pair)

    class Analytics(Calculations):
        @staticmethod
        def predict_random(number: int) -> list:
            out: list = []
            for obs in range(number):
                head: int = randint(0, 1)
                tail: int = 0 if head else 1
                out.append([head, tail])
            return out

        def predict_last(self):
            return self.data[-1]


def main() -> None:
    try:
        data: list = Research().file_reader()
        print(data)
        obj1: Research.Calculations = Research().Calculations(data)
        count: tuple = obj1.count()
        print(*count)
        fractions: tuple = obj1.fractions(count)
        print(*fractions)

        obj2: Research.Analytics = Research.Analytics(data)
        observations: list = obj2.predict_random(3)
        print(observations)
        predict_last: list = obj2.predict_last()
        print(predict_last)

    except TypeError:
        pass


if __name__ == '__main__':
    main()
