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


def check_ticker(ticker_name: str) -> tuple:
    STOCKS: dict = data_init('STOCKS')
    if ticker_name.lower() in [x.lower() for x in STOCKS.keys()]:
        return True, STOCKS[ticker_name.upper()]
    else:
        return False, 0


def get_company_name(ticker_name: str) -> str:
    COMPANIES: dict = data_init('COMPANIES')
    for c_name, c_ticker in COMPANIES.items():
        if c_ticker == ticker_name:
            return c_name


def main() -> None:
    try:
        if len(sys.argv) < 3:
            company_ticker: str = sys.argv[1]
            in_dict, stock = check_ticker(company_ticker)
            if in_dict:
                print(get_company_name(company_ticker.upper()), stock)
            else:
                print("Unknown ticker")

    except IndexError as error:
        print("ERROR:", error, "- ticker is not defined")


if __name__ == '__main__':
    main()
