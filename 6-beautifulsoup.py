# the difference between selenium and beautifulsoup is that beautifulsoup doesn't need to open browser window

from bs4 import BeautifulSoup
import requests

def currency_rate(amount, in_currency, out_currency):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={in_currency}&To={out_currency}"
    content = requests.get(url).text # here we get the source code
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('p', class_="result__BigRate-sc-1bsijpp-1 iGrAod").get_text() # here we choose the part we want

    return rate

current_rate = currency_rate(1, 'EUR', 'AZN')
print(current_rate)