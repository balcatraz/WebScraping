from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

# twilio info
accountSID = "*" # removed for security reasons

authToken = "*" # removed for security reasons

client = Client(accountSID, authToken)

twilionum = "+17625503687"

cellnum = "*" # removed for security reasons

# web scraping
url = "https://www.livecoinwatch.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

coins = soup.findAll('tr', class_="table-row filter-row")

for c in coins[:5]:
    td = c.findAll('td')

    name = td[1].findAll('small', class_="abr text-truncate")[0].text
    ticker = td[1].findAll('div', class_="filter-item-name mb0 text-left")[0].text
    price = float(td[2].text.lstrip('$'))
    changeperc = td[8].findAll('span', class_='percent')[0].text
    price24hr = price - (price * (float(changeperc.rstrip('%'))/100))

    print(f'Name: {name}\nSymbol: {ticker}\nPrice: ${format(price,".2f")}'
          + f'\n24 Hour Change: {changeperc}\nPrice 24 Hrs Ago: ${format(price24hr,".2f")}')
    print()

    if name == 'Bitcoin' and price < 40000.00:
        message = client.messages.create(to=cellnum, from_=twilionum, body='Bitcoin dropped below $40,000.00.')

    if name == 'Ethereum' and price < 3000.00:
        message = client.messages.create(to=cellnum, from_=twilionum, body='Ethereum dropped below $3,000.00.')
