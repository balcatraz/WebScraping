import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]

randChap = random.choice(chapters)

url = "https://ebible.org/asv/JHN" + randChap + ".htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

verses = soup.findAll("div", class_="p")

myverses = []

for v in verses:
    for x in v.text.split("  "):
        myverses.append(x)

mychoice = random.choice(myverses)

print(f"Chapter: {randChap} \nVerse: {mychoice}")
