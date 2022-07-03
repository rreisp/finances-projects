from hashlib import new
import requests
from bs4 import BeautifulSoup, Tag
import re
from yahoofinancials import YahooFinancials
from yahoofinancialsincomestatetement import YahooFinancialsIncomeStatement
from yahoosummary import YahooSummary

class YahooExtractor:
  @staticmethod
  def summary(stock):
    # This is a standard user-agent of Chrome browser running on Windows 10 
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
    url_pattern = 'https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch'
    url = url_pattern.format(stock, stock)
    # Use requests to retrieve data from a given URL
    response = requests.get(url, headers=headers)
    # Parse the whole HTML page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

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

    search_at = re.search(r'At close:  (.*) (.*)', soup.find('div', {"id" : "quote-market-notice"}).get_text())
    at = search_at.group(1) + ' '+ search_at.group(2)
    
    yahoo_data = YahooSummary(stock, qsp_price, previous_close, open, bid, ask, day_range, weeks52_range, 
                          volume, avg_volume, market_cap, beta, pe_ratio, eps, earnings_date, 
                          forward_dividend, ex_dividend_date, y1_target_est, at)
    return yahoo_data

  @staticmethod
  def financials(stock):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
    url_pattern = 'https://finance.yahoo.com/quote/{}/financials?p={}'
    url = url_pattern.format(stock, stock)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')


    # rows = soup.div['D(tbr) fi-row Bgc($hoverBgColor):h']

    annual_income_statements_title_rows = soup.find_all(class_ = 'D(tbr) C($primaryColor)')
    # print(len(annual_income_statements_title_rows))
    annual_income_statements_title_cols = annual_income_statements_title_rows[0].find_all('span')
    annual_income_statements_title_cols = [x.text for x in annual_income_statements_title_cols][1:6]

    annual_income_statements_rows = soup.find_all(class_ = 'D(tbr) fi-row Bgc($hoverBgColor):h')
    #rows = soup.find_all(class_ = 'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')

    annual_income_statement = []

    for row in annual_income_statements_rows:
      # print(row.find_all('span'))
      row = [x.text for x in row][1:6]
      annual_income_statement.append(row)

    annual_income_statement_obj = YahooFinancialsIncomeStatement(annual_income_statements_title_cols, 
          annual_income_statement[0], annual_income_statement[1], annual_income_statement[2], annual_income_statement[3], annual_income_statement[4], 
          annual_income_statement[5], annual_income_statement[6], annual_income_statement[7], annual_income_statement[8],annual_income_statement[9],
          annual_income_statement[10], annual_income_statement[11], annual_income_statement[12], annual_income_statement[13],annual_income_statement[14],
          annual_income_statement[15], annual_income_statement[16], annual_income_statement[17], annual_income_statement[18],annual_income_statement[19],
          annual_income_statement[20], annual_income_statement[21], annual_income_statement[22], annual_income_statement[23], annual_income_statement[24], 
          annual_income_statement[25], annual_income_statement[26], annual_income_statement[27], annual_income_statement[28],annual_income_statement[29])
    
    financials = YahooFinancials(annual_income_statement_obj)
    return financials