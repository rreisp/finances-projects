#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 15:27:06 2022

@author: rreisp
"""


import yahoofinancescraper as yf

#wege3_summary = yf.YahooExtractor.summary('WEGE3.SA')
#wege3_summary.print()

wege3_financials = yf.YahooExtractor.financials('WEGE3.SA')
wege3_financials.print()