import openpyxl
#Create new workbook
# wb = openpyxl.Workbook()
import os

#load new workbook



def loadWorkook(wb_path):
    if(os.path.exists(wb_path)):
        return openpyxl.load_workbook(wb_path)
    else:
        return openpyxl.Workbook()

WB_PATH = 'employee2.xlsx'

wb = loadWorkook(WB_PATH)

sheet = wb['Employees']

# sheet.title = "Employees"


# employees = [
#     (1,'First name','Last name','Age','Date'),
#     (2,'Thomas','Sarpong','25','12-12-20'),
#     (3,'Asamoah','Sarpong','25','12-12-20'),
#     (4,'Kofi','Sarpong','25','12-12-20'),
#     (5,'Thomas','Sarpong','25','12-12-20'),
#     (6,'Thomas','Sarpong','25','12-12-20'),
# ]

for row in sheet.values:
    for columns in row:
        print(columns)
    # print(row)

# for employee in employees:
#     sheet.append(employee)


# wb.save(WB_PATH)

