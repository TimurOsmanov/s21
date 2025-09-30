# (echo head,tail && echo 0,1 && echo 1,0 && echo 0,1 && echo 1,0 && echo 0,1 && echo 0,1 && echo 0,1 && echo 1,0 && echo 1,0 && echo 0,1 && echo 1,0 && echo 0,1) > data.csv
class Must_read:
    try:
        with open("data.csv", "r") as file:
            for line in file:
                print(line[:-1])
    except FileNotFoundError as error:
        print(f"FileNotFoundError: {error} No such file")


if __name__ == '__main__':
    Must_read()
