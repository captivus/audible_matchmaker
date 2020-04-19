'''
This file is written leveraging a tutorial available here:
https://dev.to/lewiskori/introduction-to-web-scraping-with-python-24li
'''

import requests, json
from bs4 import BeautifulSoup

# configure user agent
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

# configure base URL
base_url = "https://www.amazon.com/hz/audible/matchmaker?_encoding=UTF8&ref_=wfv_featuredoc_mm"

# create initial request and save response object
r = requests.get(base_url, headers=header)

print(r)

soup = BeautifulSoup(markup=r.text, features='html.parser')
print(soup.prettify())


if r.status_code == 200:
    soup = BeautifulSoup(markup=r.text, features='html.parser')
    upgrade_prices = soup.findAll(name="a-size-base.a-color-price.a-text-bold", )

    pass
else:
    pass

