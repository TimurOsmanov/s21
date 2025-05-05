import sys


def cipher(text: str, shift: int) -> str:
    out: str = ''
    upper_letters: list = [x + 65 for x in range(26)]
    lower_letters: list = [x + 97 for x in range(26)]

    for letter in text:
        if ord(letter) > 127:
            out = f"LanguageSupportError: symbol '{letter}' - the script does not support your language yet"
            break
        elif 64 < ord(letter) < 91:
            new_index: int = (upper_letters.index(ord(letter)) + shift % 26) % 26
            out += chr(upper_letters[new_index])
        elif 96 < ord(letter) < 123:
            new_index: int = (lower_letters.index(ord(letter)) + shift % 26) % 26
            out += chr(lower_letters[new_index])
        else:
            out += letter

    return out


def argv_check(my_argv: list) -> list:
    if len(my_argv) != 4:
        # if there is incorrect num of args
        return []

    return my_argv[1:]


def main() -> None:
    try:
        argv_checked: list = argv_check(sys.argv)

        mode_from_args: str; text_from_args: str; shift_from_args: str
        mode_from_args, text_from_args, shift_from_args = argv_checked

        shift_dict: dict = {"encode": int(shift_from_args), "decode": -int(shift_from_args)}
        cipher_shift: int = shift_dict[mode_from_args]

        print(cipher(text_from_args, cipher_shift))

    except ValueError as error:
        print(f"ValueError: {error} - wrong args number")

    except KeyError as mode_error:
        print(f"KeyError: {mode_error} - wrong cipher mode name")


if __name__ == '__main__':
    main()
