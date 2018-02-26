import json
from collections import Counter
from enum import Enum


class Month(Enum):
    January = '01'
    February = '02'
    March = '03'
    April = '04'
    May = '05'
    June = '06'
    July = '07'
    August = '08'
    September = '09'
    October = '10'
    November = '11'
    December = '12'


def extractMonthsFromDict(bdayList):
    listOfMonths = []
    for date in bdayList.values():
        currKey = date.split('/')[0]
        monthName = str(Month(currKey))
        listOfMonths.append(monthName.split('.')[1])
    return listOfMonths


with open('birthdays.json', 'r') as jsonFile:
    birthdays = json.load(jsonFile)
    c = Counter(extractMonthsFromDict(birthdays))
    for month, count in c.items():
        print(month + ":", count)







