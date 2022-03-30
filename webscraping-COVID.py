# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from cgitb import text
from turtle import title
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


url = "https://www.worldometers.info/coronavirus/country/us"
# Request in case 404 Forbidden error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

title = soup.title

print(title.text)

tableRows = soup.findAll("tr")


highestDeath = 0
highTestRatio = 0
lowestTest = 9999

highestDeathSt = ""
highTestRatioSt = ""
lowestTestSt = ""

for x in tableRows[2:52]:
    td = x.findAll("td")

    state = td[1].text.replace("\n", "")
    totCases = int(td[2].text.replace(",", ""))
    totDeaths = int(td[4].text.replace(",", ""))
    totTests = int(td[10].text.replace(",", ""))

    print(f"State: {state}")
    print(f"Total Cases: {totCases}")
    print(f"Total Deaths: {totDeaths}")
    print(f"Total Tests: {totTests}")

    print(f"Test Ratio: {round(totCases/totTests,2)}")
    print(f"Death Ratio: {round(totDeaths/totCases,2)}")
    print()

    if totDeaths > highestDeath:
        highestDeath = totCases
        highestDeathSt = state

    if totCases / totTests > highTestRatio:
        highTestRatio = totCases / totTests
        highTestRatioSt = state

    if totCases / totTests < lowestTest:
        lowestTest = totCases / totTests
        lowestTestSt = state

print(f"Highest Deaths: {highestDeath} in {highestDeathSt}")
print(f"Highest Test Ratio: {round(highTestRatio*100,2)}% in {highTestRatioSt}")
print(f"Lowest Test Ratio: {round(lowestTest*100,2)}% in {lowestTestSt}")

# SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
# -----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

# Tags: find("h1","h2","h3", etc.)
# Attributes: find("span", {"class":{"green","red"}})
# Text: nameList = Objfind(text="the prince")
# Limit = find with limit of 1
# keyword: allText = Obj.find(id="title",class="text")

# HTML tags
# <span> <h1> <p>
# <table> <tr> <td>
#
