from openpyxl import Workbook
import openpyxl as pyxl

def grade_point_from_letter(1):
    l_s_map = {"S":9}



wb = pyxl.load_workbook("student.xlsx")
sheet = wb.active
for row in sheet.iter_rows(min_row = 3, min_col = 2, max_row = 4, max_col = 3):
    if row:
        data = [c.value for c in row]
        