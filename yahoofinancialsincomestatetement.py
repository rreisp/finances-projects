import pandas as pd


class YahooFinancialsIncomeStatement:
    def __init__(self, title, total_revenue, cost_of_revenue, gross_profit, operating_expense, operating_income, net_non_operating_interest_income_expense, pretax_income, tax_provision,
                 net_income_common_stockholders, diluted_ni_available_to_com_stockholders, basic_eps, diluted_eps, basic_average_shares, diluted_average_shares, total_expenses,
                 net_income_from_continuing_discontinued_operation, normalized_income, interest_income, interest_expense, net_interest_income, ebit, ebtida, reconciled_cost_of_revenue,
                 reconciled_depreciation, net_income_from_continuing_operation_net_minority_interest, total_unusual_items_excluding_goodwill, total_unusual_items, normalized_ebitda,
                 tax_rate_for_calcs, tax_effect_of_unusual_items):
        self.title = title
        self.total_revenue = total_revenue
        self.cost_of_revenue = cost_of_revenue
        self.gross_profit = gross_profit
        self.operating_expense = operating_expense
        self.operating_income = operating_income
        self.net_non_operating_interest_income_expense = net_non_operating_interest_income_expense
        self.pretax_income = pretax_income
        self.tax_provision = tax_provision
        self.net_income_common_stockholders = net_income_common_stockholders
        self.diluted_ni_available_to_com_stockholders = diluted_ni_available_to_com_stockholders
        self.basic_eps = basic_eps
        self.diluted_eps = diluted_eps
        self.basic_average_shares = basic_average_shares
        self.diluted_average_shares = diluted_average_shares
        self.total_expenses = total_expenses
        self.net_income_from_continuing_discontinued_operation = net_income_from_continuing_discontinued_operation
        self.normalized_income = normalized_income
        self.interest_income = interest_income
        self.interest_expense = interest_expense
        self.net_interest_income = net_interest_income
        self.ebit = ebit
        self.ebtida = ebtida
        self.reconciled_cost_of_revenue = reconciled_cost_of_revenue
        self.reconciled_depreciation = reconciled_depreciation
        self.net_income_from_continuing_operation_net_minority_interest = net_income_from_continuing_operation_net_minority_interest
        self.total_unusual_items_excluding_goodwill = total_unusual_items_excluding_goodwill
        self.total_unusual_items = total_unusual_items
        self.normalized_ebitda = normalized_ebitda
        self.tax_rate_for_calcs = tax_rate_for_calcs
        self.tax_effect_of_unusual_items = tax_effect_of_unusual_items

    def dataframe(self):
        data = {
            'Total Revenue': self.total_revenue,
            'Cost of Revenue': self.cost_of_revenue,
            'Gross Profit': self.gross_profit,
            'Operating Expense': self.operating_expense,
            'Operating Income': self.operating_income,
            'Net Non Operating Interest Income Expense': self.net_non_operating_interest_income_expense,
            'Pretax Income': self.pretax_income,
            'Tax Provision': self.tax_provision,
            'Net Income Common Stockholders': self.net_income_common_stockholders,
            'Diluted NI Available to Com Stockholders': self.diluted_ni_available_to_com_stockholders,
            'Basic EPS': self.basic_eps,
            'Diluted EPS': self.diluted_eps,
            'Basic Average Shares': self.basic_average_shares,
            'Diluted Average Shares': self.diluted_average_shares,
            'Total Expenses': self.total_expenses,
            'Net Income from Continuing & Discontinued Operation': self.net_income_from_continuing_discontinued_operation,
            'Normalized Income': self.normalized_income,
            'Interest Income': self.interest_income,
            'Interest Expense': self.interest_expense,
            'Net Interest Income': self.net_interest_income,
            'EBIT': self.ebit,
            'EBITDA': self.ebtida,
            'Reconciled Cost of Revenue': self.reconciled_cost_of_revenue,
            'Reconciled Depreciation': self.reconciled_depreciation,
            'Net Income from Continuing Operation Net Minority Interest': self.net_income_from_continuing_operation_net_minority_interest,
            'Total Unusual Items Excluding Goodwill': self.total_unusual_items_excluding_goodwill,
            'Total Unusual Items': self.total_unusual_items,
            'Normalized EBITDA': self.normalized_ebitda,
            'Tax Rate for Calcs': self.tax_rate_for_calcs,
            'Tax Effect of Unusual Items': self.tax_effect_of_unusual_items
        }
        df = pd.DataFrame(data)
        # df.index =  self.title[1:]
        df = df.transpose()
        # df.index = self.title[1:]
        return df

    def print(self):
        print("Title\t\t", self.title)
        print("Total Revenue\t", self.total_revenue)
        print("Cost of Revenue\t", self.cost_of_revenue)
        print()
