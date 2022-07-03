class YahooSummary:
  def __init__(self, title, qsp_price, previous_close, open, bid, ask, day_range, weeks52_range, volume, avg_volume,
               maket_cap, beta, pe_ratio, eps, earnings_date, forward_dividend, ex_dividend_date, y1_target_est, at):
               
    self.title = title
    self.qsp_price = qsp_price
    self.previous_close = previous_close
    self.open = open
    self.bid = bid
    self.ask = ask
    self.day_range = day_range
    self.weeks52_range = weeks52_range
    self.volume = volume
    self.avg_volume = avg_volume
    self.maket_cap = maket_cap
    self.beta = beta
    self.pe_ratio = pe_ratio
    self.eps = eps
    self.earnings_date = earnings_date
    self.forward_dividend = forward_dividend
    self.ex_dividend_date = ex_dividend_date
    self.y1_target_est = y1_target_est
    self.at = at

  def print(self):
    print("**  \t"+ self.title + "\t  **")
    print("qsp-price\t", self.qsp_price)
    print("previous-close\t", self.previous_close)
    print("open\t\t", self.open)
    print("bid\t\t", self.bid)
    print("ask\t\t", self.ask)
    print("day's-range\t", self.day_range)
    print("52-weeks-range\t", self.weeks52_range)
    print("volume\t\t", self.volume)
    print("avg-volume\t", self.avg_volume)
    print("market-cap\t", self.maket_cap)
    print("beta-5y\t\t", self.beta)
    print("pe-ration\t", self.pe_ratio)
    print("eps\t\t", self.eps)
    print("earnings-date\t", self.earnings_date)
    print("forward-dividend", self.forward_dividend)
    print("ex-dividend-date", self.ex_dividend_date)   
    print("1-y-target-est\t", self.y1_target_est)
    print("at\t\t", self.at)
    print()