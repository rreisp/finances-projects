class YahooFinancials:
  def __init__(self, annual_income_statement):
    self.annual_income_statement = annual_income_statement

  def print(self):
    self.annual_income_statement.print()
    print()