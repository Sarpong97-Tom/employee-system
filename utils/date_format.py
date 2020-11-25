import datetime,calendar

from datetime import date

def getTodaysDate():
    return datetime.date.today()

def getAge(date):
    today = datetime.date.today()
    print(datetime.datetime.now())
    # date = convertStringToDate(date)
    
    yearDiff = today.year - int(date.year)
    monthDiff = today.month - int(date.month)
    if monthDiff <6:
        age = yearDiff
    else:
        age = yearDiff+1
    return age

# myage = getAge(now)
# print(myage)
