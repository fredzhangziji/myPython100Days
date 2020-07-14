'''
Get the number of days with the dates.
    12/27/2019
    written by Fred Zhang
'''

def isLeapYear(year):
    if year % 100 == 0:
        return True if year % 400 == 0 else False
    else:
        return True if year % 4 == 0 else False

def datesToDays(month, date, year):
    bigMonth = (1,3,5,7,8,10,12)
    smallMonth = (4,6,9,11)
    numDays = 0
    if isLeapYear == True:
        for x in range(1, month):
            if x in bigMonth:
                numDays += 31
            elif x in smallMonth: 
                numDays += 30
            else:
                numDays += 29
    else:
        for x in range(1, month):
            if x in bigMonth:
                numDays += 31
            elif x in smallMonth: 
                numDays += 30
            else:
                numDays += 28
    return numDays+date

if __name__ == '__main__':
    print(datesToDays(10,21,2019))
