# before start py-script run in terminal command below (to dwnld ds.csv)
# curl -L -o ds.csv "https://drive.google.com/uc?export=download&id=1tDEDTytYaUrfJsXD5z5QvJSb5VNlL-eZ"

def read_csv() -> list:
      out: list = []
      with open("ds.csv", "r") as file:
            for line in file:
                  line_spltd: list = []

                  v_id, created, name, other = line.split('",')
                  for col in v_id, created, name:
                        line_spltd.append(col + '"')

                  for col in other.split(','):
                        line_spltd.append(col)
                  out.append(line_spltd)
      return out


def replace_delim(my_list:list) -> list:
      out: list = ['\t'.join(line) for line in my_list]
      return out


def write_tsv(my_list:list) -> None:
      with open("ds.tsv", "w") as file:
            for line in my_list:
                  file.write(line)


def main() -> None:
      try:
            text: list = read_csv()
            replaced: list = replace_delim(text)
            write_tsv(replaced)
      except FileNotFoundError as error:
            # forget to run curl command
            print(f"{error} No such file")


if __name__ == '__main__':
      main()
