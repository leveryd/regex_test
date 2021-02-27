"""
https://github.com/scrapinghub/dateparser/issues/869
"""

from dateparser.search import search_dates

search_dates("?"*100000+"x")
