from openpyxl import Workbook


def get_xlsx():
    wb = Workbook()
    wb.save("test.xlsx")
