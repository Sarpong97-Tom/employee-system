import openpyxl
import os

class ExcelHelper:
    def loadFile(self,file):
        self.wb = openpyxl.load_workbook(file)

    def getRowDict(self,file,sheet):
        listDict = []
        wb = self.loadFile(file)
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

    

