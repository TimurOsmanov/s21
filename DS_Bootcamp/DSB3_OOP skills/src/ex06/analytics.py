import sys
from random import randint
import logging
import requests


class Research:
    logging.basicConfig(level=logging.INFO,
                        filename="analytics.log",
                        filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    def __init__(self) -> None:
        try:
            self.path: str = sys.argv[1]
            logging.info(f"init class Research with {self.path}")
        except IndexError as error:
            self.path = ''
            logging.error(f"init class Research: {error}")

    def file_reader(self, has_header: bool = True) -> list:
        out: list = []
        try:
            with open(self.path, "r") as file:
                lines_count: int = 0
                counter: int = 0 if has_header else -1
                for num, line in enumerate(file.read().split("\n")):
                    head, tail = line.split(",")
                    if num != counter:
                        if int(head) + int(tail) != 1:
                            out = ["ValueError: wrong structure/data"]
                            break
                        out.append([int(head), int(tail)])
                        lines_count += 1
            logging.info(f"class Research method file_reader with {self.path}")
            if lines_count < 1:
                out = [f"ValueError: wrong structure/data"]
                logging.error(f"class Research method file_reader: {out}")
        except FileNotFoundError as error:
            out = [f"FileNotFoundError: {error} No such file"]
            logging.error(f"class Research method file_reader: {out}")

        except ValueError as error:
            out = [f"ValueError: {error} wrong structure/data"]
            logging.error(f"class Research method file_reader: {out}")

        return out

    @staticmethod
    def tg_msg(text: str):
        bot_token: str = 'your bot'
        chat_id: str = 'your chat'
        webhook: str = f'https://api.telegram.org/{bot_token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(webhook)
        logging.info(f"class Research method tg_msg")

    class Calculations:
        def __init__(self, data) -> None:
            self.data = data
            logging.info(f"class Calculations init with {self, data}")

        def count(self) -> tuple[int, int]:
            head_sum: int = 0
            tail_sum: int = 0
            for pair in self.data:
                head_sum += pair[0]
                tail_sum += pair[1]
            logging.info(f"class Calculations method count with {self.data}")
            return head_sum, tail_sum

        @staticmethod
        def fractions(pair: tuple) -> tuple[float, float]:
            logging.info(f"class Calculations method fractions with {pair}")
            return pair[0] / sum(pair), 1 - pair[0] / sum(pair)

    class Analytics(Calculations):
        @staticmethod
        def predict_random(number: int) -> list:
            out: list = []
            for obs in range(number):
                head: int = randint(0, 1)
                tail: int = 0 if head else 1
                out.append([head, tail])
            logging.info(f"class Analytics(Calculations) method predict_random with num = {number}")
            return out

        def predict_last(self) -> list:
            logging.info(f"class Analytics(Calculations) method predict_last")
            return self.data[-1]

        @staticmethod
        def save_file(name, ext, data) -> None:
            with open(f"{name}.{ext}", "w") as file:
                file.write(data)
            logging.info(f"class Analytics(Calculations) method save_file")
