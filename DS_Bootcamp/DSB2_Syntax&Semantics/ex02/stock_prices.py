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


def check_name(name: str) -> tuple:
    COMPANIES: dict = data_init('COMPANIES')
    if name.lower() in [x.lower() for x in COMPANIES.keys()]:
        return True, COMPANIES[name.lower().capitalize()]
    else:
        return False, 0


def get_quot(ticker: str) -> float:
    STOCKS: dict = data_init('STOCKS')
    return STOCKS[ticker]


def main() -> None:
    try:
        if len(sys.argv) < 3:
            company: str = sys.argv[1]
            in_dict, stock = check_name(company)
            if in_dict:
                print(get_quot(stock))
            else:
                print("Unknown company")

    except IndexError as error:
        print("ERROR:", error, "- company name is not defined")


if __name__ == '__main__':
    main()
