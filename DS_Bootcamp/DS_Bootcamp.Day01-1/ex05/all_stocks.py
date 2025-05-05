import sys


def data_init(dict_name: str) -> dict:
    COMPANIES: dict = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS: dict = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    out: dict = {
        'COMPANIES': COMPANIES,
        'STOCKS': STOCKS
    }

    return out[dict_name]


def get_company_name(ticker_name: str) -> str:
    COMPANIES: dict = data_init('COMPANIES')
    for c_name, c_ticker in COMPANIES.items():
        if c_ticker == ticker_name:
            return c_name


def check_data(element: str) -> tuple:
    COMPANIES: dict = data_init('COMPANIES')
    STOCKS: dict = data_init('STOCKS')
    out: tuple = "unknown", (element, '')
    for c_name, c_ticker in COMPANIES.items():
        if c_ticker.lower() == element.lower():
            # the program should not be case-sensitive
            out = "ticker", (c_ticker, get_company_name(c_ticker))
        elif c_name.lower() == element.lower():
            # the program should not be case-sensitive
            out = "company", (c_name, STOCKS[c_ticker])
    return out


def argv_check(my_argv: list) -> list:
    if len(my_argv) != 2:
        # if there are no arguments or too many arguments, the program displays nothing
        return []

    argv: list = sys.argv[1].split(",")
    argv = [value.strip() for value in argv]
    # the program should be able to work with white spaces

    if not all(argv):
        # when there are two commas in a row in the string, the program does not display anything
        # 2 commas in a row = one or more empty value in data all(argv) = False in that case
        return []

    return argv


def main() -> None:
    data: list = argv_check(sys.argv)
    if data:
        for elem in data:
            elem_type, type_data_pair = check_data(elem)
            out_dict: dict = {
                "ticker": "is a ticker symbol for",
                "company": "stock price is",
                "unknown": "is an unknown company or an unknown ticker symbol"
            }
            if elem_type == "unknown":
                print(f"{type_data_pair[0]} {out_dict[elem_type]}")
            else:
                print(f"{type_data_pair[0]} {out_dict[elem_type]} {type_data_pair[1]}")


if __name__ == '__main__':
    main()
