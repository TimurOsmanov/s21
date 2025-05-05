#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup
import urllib3
# profiling num3 python -m cProfile -s time ./financial_enhanced.py msft 'Gross Profit' > profiling-http.txt
# profiling num4 python -m cProfile -s ncalls ./financial_enhanced.py msft 'Gross Profit' > profiling-ncalls.txt
# profiling num5 python -m cProfile -o fin.profile ./financial_enhanced.py msft 'Gross Profit'
# profiling num5 (echo -e 'sort cumulative\nstats 5' | python3 -m pstats fin.profile) > pstats-cumulative.txt


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 3:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, ticker, cat = my_argv
    return ticker,cat


# async def a_get(url: str, headers: dict):
#     async with aiohttp.ClientSession(headers=headers, max_line_size=8190 * 2, max_field_size=8190 * 2) as session:
#         async with session.get(url) as response:
#             return await response.read()


def parce(ticker: str) -> bytes:
    url = f'https://finance.yahoo.com/quote/{ticker.upper()}/financials'
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response = urllib3.request("GET", url, headers=headers)
        # response = asyncio.run(a_get(url, headers))
        return response.data
    except Exception as e:
        print(f"Error: {e}")


def get_data(page: bytes, cat: str) -> list:
    soup = BeautifulSoup(page, "html.parser")
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
        ticker, cat = argv_check(sys.argv)
        page = parce(ticker)
        return get_data(page, cat)[0]

    except ValueError as error:
        return f"ValueError: {error} - wrong task name"
    except IndexError:
        return "Wrong name of ticker or category"


if __name__ == '__main__':
    print(main())
