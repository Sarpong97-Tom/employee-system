import openpyxl
import os

class ExcelHelper:
        file = None
        wb = None
    def __init__(self, file):
        self.file = file
    def loadFile(self):
        self.wb = openpyxl.load_workbook(self.file)

    def getRowDict(self,sheet,form):
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

    

