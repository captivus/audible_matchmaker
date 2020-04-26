import requests
from bs4 import BeautifulSoup

# open Audible Matchmaker page locally
# (see accompanying Jupyter notebook for details)
infile = open(file='audible_matchmaker.html', mode='r')

# parse the page with BeautifulSoup
soup = BeautifulSoup(markup=infile, features='html.parser')

# find all of the spans containing the audiobook price 
# (see accompanying Jupyter notebook for details)
upgrade_prices = soup.findAll(name='span', attrs={'class' : 'a-size-base a-color-price a-text-bold'})

# initialize some variables to process & sum prices
total_upgrade_price = 0
string = 's'

# iterate over each of the book prices
for book in upgrade_prices:
    # convert the span price data to a string
    price_string = book.string
    # remove the dollar sign from the price string
    price_string = price_string.replace('$', '')
    # convert the price string to a decimal number
    price = float(price_string)
    # add it to our running total
    total_upgrade_price += price

# Donezo!  What's it cost to buy all available Audible books?
print(total_upgrade_price)