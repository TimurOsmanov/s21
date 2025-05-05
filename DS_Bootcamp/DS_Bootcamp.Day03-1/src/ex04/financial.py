#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup
import requests
import time
# to run ./financial.py 'MSFT' 'Total Revenue'
# profiling num1 python -m cProfile -s time ./financial.py msft 'Gross Profit' > profiling-sleep.txt
# profiling num2 python -m cProfile -s time ./financial.py msft 'Gross Profit' > profiling-tottime.txt


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 3:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, ticker, cat = my_argv
    return ticker,cat


def parce(ticker: str) -> requests.models.Response:
    url = f'https://finance.yahoo.com/quote/{ticker.upper()}/financials'
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response = requests.get(url, headers=headers)
        return response
    except requests.ConnectionError as e:
        print(f"Error: {e}")
    except requests.Timeout as e:
        print(f"Error: {e}")
    except requests.RequestException as e:
        print(f"Error: {e}")


def get_data(page: requests.models.Response, cat: str) -> list:
    soup = BeautifulSoup(page.text, "html.parser")
    titles = soup.find_all("div", class_='row lv-0 yf-t22klz')
    out: dict = {}
    for line in titles:
        col_name: str = line.find("div", class_='rowTitle yf-t22klz').text
        out[col_name] = []
        odd_cols = line.find_all("div", class_='column yf-t22klz alt')
        for num, odd in enumerate(odd_cols):
            out[col_name].append((num * 2 + 1, odd.text.strip()))
        even_cols = line.find_all("div", class_='column yf-t22klz')
        for num, even in enumerate(even_cols):
            out[col_name].append((num * 2 + 2, even.text.strip()))

    try:
        return [(cat, *(x[1] for x in sorted(out[cat])))]
    except KeyError:
        return []


def main() -> str | tuple:
    try:
        # time.sleep(5)
        ticker, cat = argv_check(sys.argv)
        page = parce(ticker)
        return get_data(page, cat)[0]

    except ValueError as error:
        return f"ValueError: {error} - wrong task name"
    except IndexError:
        return f"Wrong name of ticker or category"


if __name__ == '__main__':
    print(main())
