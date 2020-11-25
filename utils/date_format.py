import datetime,calendar

from datetime import date

# date_string = '2015-01-30'
# now = date(*map(int, date_string.split('-')))
# print(now)

# def convertStringToDate(date):

#     return datetime.datetime.strftime(date,'%y-%d-%m')

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
