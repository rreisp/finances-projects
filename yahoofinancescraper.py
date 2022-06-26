import requests
from bs4 import BeautifulSoup
import re

from yahoosummary import YahooSummary

class YahooExtractor:
  def __init__(self):
    print()

  @staticmethod
  def summary(stock):
    # This is a standard user-agent of Chrome browser running on Windows 10 
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
    
    url_pattern = 'https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'

    # Use requests to retrieve data from a given URL
    url = url_pattern.format(stock, stock)
    print(url)
    response = requests.get(url, headers=headers)

    # Parse the whole HTML page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Title of the parsed page
    # print(soup.title)

    qsp_price = soup.find('fin-streamer', {"data-test" : "qsp-price"}).get_text()
    previous_close = soup.find('td', {"data-test" : "PREV_CLOSE-value"}).get_text()
    open = soup.find('td', {"data-test" : "OPEN-value"}).get_text()
    bid = soup.find('td', {"data-test" : "BID-value"}).get_text()
    ask = soup.find('td', {"data-test" : "ASK-value"}).get_text()
    day_range = soup.find('td', {"data-test" : "DAYS_RANGE-value"}).get_text()
    weeks52_range = soup.find('td', {"data-test" : "FIFTY_TWO_WK_RANGE-value"}).get_text()
    volume = soup.find('fin-streamer', {"data-field" : "regularMarketVolume"}).get_text()
    avg_volume = soup.find('td', {"data-test" : "AVERAGE_VOLUME_3MONTH-value"}).get_text()
    market_cap = soup.find('td', {"data-test" : "MARKET_CAP-value"}).get_text()
    beta = soup.find('td', {"data-test" : "BETA_5Y-value"}).get_text()
    pe_ratio = soup.find('td', {"data-test" : "PE_RATIO-value"}).get_text()
    eps = soup.find('td', {"data-test" : "EPS_RATIO-value"}).get_text()
    earnings_date = soup.find('td', {"data-test" : "EARNINGS_DATE-value"}).get_text()
    forward_dividend = soup.find('td', {"data-test" : "DIVIDEND_AND_YIELD-value"}).get_text()
    ex_dividend_date = soup.find('td', {"data-test" : "EX_DIVIDEND_DATE-value"}).get_text()
    y1_target_est = soup.find('td', {"data-test" : "ONE_YEAR_TARGET_PRICE-value"}).get_text()
    #at = re.search(r'At close:\.(.*?)', soup.find('div', {"id" : "quote-market-notice"}).get_text()).group(1)
    search_at = re.search(r'At close:  (.*) (.*)', soup.find('div', {"id" : "quote-market-notice"}).get_text())
    at = search_at.group(1) + ' '+ search_at.group(2)
    
    yahoo_data = YahooSummary(stock, qsp_price, previous_close, open, bid, ask, day_range, weeks52_range, 
                          volume, avg_volume, market_cap, beta, pe_ratio, eps, earnings_date, 
                          forward_dividend, ex_dividend_date, y1_target_est, at)
    return yahoo_data 