import openpyxl
def checkduplicateEmails(list_email,new_email):
    if len(list_email)>0:
        for email in list_email:
            if email ==  new_email:
                return True
            else:
                return False
    else:
        return False

def loadWorksheet(wb):
    wb = openpyxl.load_workbook(wb)
    sheet =  wb.worksheets[0]
    return sheet

    
