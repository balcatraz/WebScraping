from os import name
import openpyxl as xl
from openpyxl.styles import Font

# create a enw excel document
wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "First Sheet"


# create a new workbook
wb.create_sheet(index=1, title="Second Sheet")

# write content to cell
MySheet["A1"] = "An example of Sum Formula"

# change the font size and italicize
MySheet["A1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

# alternatively create a font object
fontObj = Font(name="Times New Roman", size=24, italic=True, bold=True)

MySheet["A1"].font = fontObj

# adding values to cells
MySheet["B2"] = 50
MySheet["B3"] = 75
MySheet["B4"] = 100

MySheet["A6"] = "Total"
MySheet["A6"].font = Font(size=16, bold=True)

MySheet["B6"] = "=SUM(B2:B5)"

# change the column width
MySheet.column_dimensions["A"].width = 25


wb.save("PythonToExcel.xlsx")
