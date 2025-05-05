class Research:
    @staticmethod
    def file_reader() -> str:
        out: str = ""
        try:
            with open("data.csv", "r") as file:
                for line in file:
                    out += line[:-1] + '\n'
        except FileNotFoundError as error:
            out = f"FileNotFoundError: {error} No such file "
        return out[:-1]


if __name__ == '__main__':
    print(Research.file_reader())
