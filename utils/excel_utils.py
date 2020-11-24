import openpyxl
import os

class ExcelHelper:
        file = None
        wb = None
    def __init__(self, file):
        self.file = file
    def loadFile(self):
        self.wb = openpyxl.load_workbook(self.file)

    def getRowTuple(self,sheet,form):
        listDict = []
        wb = self.loadFile()
        sheet = wb[sheet]
        for row in sheet:
           for firs_tname, last_name,email,password,date_of_birth,date_of_employment,position,salary,is_supervisor in row:
               listDict.append({
                   'firs_tname':firs_tname,
                   'last_name':last_name,
                   'email':email,
                   'password':password,
                   'date_of_birth':date_of_birth,
                   'date_of_employment':date_of_employment,
                   'position':position,
                   'salary':salary,
                   'is_supervisor':is_supervisor,
                   })
        return listDict

    


    

# #load new workbook



# def loadWorbook(wb_path):
#     if(os.path.exists(wb_path)):
#         return openpyxl.load_workbook(wb_path)
#     else:
#         return openpyxl.Workbook()

# WB_PATH = 'employee2.xlsx'

# wb = loadWorkook(WB_PATH)

# sheet = wb['Employees']

# # sheet.title = "Employees"


# # employees = [
# #     (1,'First name','Last name','Age','Date'),
# #     (2,'Thomas','Sarpong','25','12-12-20'),
# #     (3,'Asamoah','Sarpong','25','12-12-20'),
# #     (4,'Kofi','Sarpong','25','12-12-20'),
# #     (5,'Thomas','Sarpong','25','12-12-20'),
# #     (6,'Thomas','Sarpong','25','12-12-20'),
# # ]

# for row in sheet.values:
#     for columns in row:
#         print(columns)
#     # print(row)

# # for employee in employees:
# #     sheet.append(employee)


# # wb.save(WB_PATH)

