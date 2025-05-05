#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib3
# py.test -v ./financial_test.py
# py.test -q ./financial_test.py


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 3:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, ticker, cat = my_argv
    return ticker,cat


def parce(ticker: str) -> bytes:
    url = f'https://finance.yahoo.com/quote/{ticker.upper()}/financials'
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
        response = urllib3.request("GET", url, headers=headers)
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


def main(ticker: str, cat:str) -> str | tuple:
    try:
        ticker, cat = argv_check(["financial_test.py", ticker, cat])
        page = parce(ticker)
        return get_data(page, cat)[0]
    except ValueError as error:
        return f"ValueError: {error} - wrong task name"
    except IndexError:
        return "Error: Wrong name of ticker or category"


def test_argv_check_msft_total_revenue() -> None:
    ticker, cat = argv_check(["financial_test.py", "msft", "Total Revenue"])
    assert ticker == "msft"
    assert cat == "Total Revenue"


def test_argv_check_return_type() -> None:
    out = argv_check(["financial_test.py", "msft", "Total Revenue"])
    assert isinstance(out, tuple) == True


def test_argv_check_exception() -> None:
    out = argv_check(["financial_test.py", "msft", "Total Revenue", 'value'])
    assert out == ()


def test_parce_msft() -> None:
    parsed = parce("MSFT")
    soup = BeautifulSoup(parsed, "html.parser")
    page = soup.find_all("html", attrs={'class': "desktop neo-green dock-upscale"})
    out = ''
    for elem in page:
        for link in elem.find_all('title'):
            out = link.text
    assert ('MSFT' in out) == True


def test_parce_return_type() -> None:
    out = parce("MSFT")
    assert isinstance(out, bytes) == True


def test_parce_exception() -> None:
    parsed = parce("123sd")
    soup = BeautifulSoup(parsed, "html.parser")
    page = soup.find_all("html", attrs={'class': "desktop neo-green dock-upscale"})
    out = ''
    for elem in page:
        for link in elem.find_all('title'):
            out = link.text
    assert out == 'Symbol Lookup from Yahoo Finance'


def test_get_data_msft_total_revenue() -> None:
    parsed = parce("MSFT")
    out = get_data(parsed, "Total Revenue")
    corr_val = [(
    'Total Revenue', '254,190,000.00', '245,122,000.00', '211,915,000.00', '198,270,000.00', '168,088,000.00')]
    assert out == corr_val


def test_get_data_return_type() -> None:
    parsed = parce("MSFT")
    out = get_data(parsed, "Total Revenue")
    assert isinstance(out, list) == True


def test_get_data_exception() -> None:
    parsed = parce("MSFT")
    out = get_data(parsed, "Sotal Revenue")
    assert out == []


def test_main_msft_total_revenue() -> None:
    out = main("msft", "Total Revenue")
    corr_val = ('Total Revenue', '254,190,000.00', '245,122,000.00', '211,915,000.00', '198,270,000.00', '168,088,000.00')
    assert out == corr_val


def test_main_return_type() -> None:
    out = main("msft", "Total Revenue")
    assert isinstance(out, tuple) == True


def test_main_exception() -> None:
    out = main("msfsssst", "Total Revenue")
    assert isinstance(out, str) == True
