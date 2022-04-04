from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


url = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

title = soup.title

print(title.text)

companies = soup.findAll("span", attrs={"class": "tv-screener__description"})

for c in companies[:5]:
    print(c.text.strip())


# SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
# -----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

# Tags: find("h1","h2","h3", etc.)
# Attributes: find("span", {"class":{"green","red"}})
# Text: nameList = Objfind(text="the prince")
# Limit = find with limit of 1
# keyword: allText = Obj.find(id="title",class="text")

stock_table = soup.findAll("tbody")

stock_table = stock_table[0]

rows = stock_table.findAll("tr")

for r in rows[:5]:
    c = r.findAll("td")
    name = (
        c[0]
        .findAll("span", attrs={"class": "tv-screener__description"})[0]
        .text.strip()
    )
    price = float(c[1].text)
    pct_change = float(c[2].text.strip("%"))
    chg = float(c[3].text)

    s_price = round(price / (1 + (pct_change / 100)), 2)

    print(f"Company Name: {name}")
    print(f"Current Price: {price}")
    print(f"Change Percent: {pct_change}%")
    print(f"Total Change: {chg}")
    print(f"Starting Price: {s_price}")
