from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
data = [
    ('id','wname','year'),
    (1002,'Max',2019),
    (1003,'KOTE',2016),
    (1004,'Joy',2017)

]
for row in data:
    sheet.append(row)
wb.save("student.xlsx")