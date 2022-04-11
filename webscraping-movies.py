from sre_constants import GROUPREF_EXISTS
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


# webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = "https://www.boxofficemojo.com/year/2022/"

page = urlopen(webpage)

soup = BeautifulSoup(page, "html.parser")

title = soup.title

print(title.text)

wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "Box Office Report"

MySheet["A1"] = "Rank"
MySheet["B1"] = "Title"
MySheet["C1"] = "Release Date"
MySheet["D1"] = "Gross"
MySheet["E1"] = "Total Gross"
MySheet["F1"] = "% of Total"

HeaderFont = Font(size=16, bold=True)

MySheet["A1"].font = HeaderFont
MySheet["B1"].font = HeaderFont
MySheet["C1"].font = HeaderFont
MySheet["D1"].font = HeaderFont
MySheet["E1"].font = HeaderFont
MySheet["F1"].font = HeaderFont

movies_table = soup.find("table")

rows = movies_table.findAll("tr")

xlCols = ["A", "B", "C", "D", "E", "F"]

for r in range(1, 6):
    td = rows[r].findAll("td")

    ranking = td[0].text
    title = td[1].text
    gross = td[5].text
    total_gross = td[7].text

    MySheet["A" + str(r + 1)] = ranking
    MySheet["B" + str(r + 1)] = title
    MySheet["C" + str(r + 1)] = td[8].text
    MySheet["D" + str(r + 1)] = gross
    MySheet["E" + str(r + 1)] = total_gross
    MySheet["F" + str(r + 1)] = (
        str(
            round(
                float(gross.replace(",", "").lstrip("$").rstrip())
                / float(total_gross.replace(",", "").lstrip("$").rstrip())
                * 100,
                2,
            )
        )
        + "%"
    )

##
##
##
##

wb.save("BoxOfficeReport.xlsx")
