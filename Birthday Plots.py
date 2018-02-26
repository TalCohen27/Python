from bokeh.plotting import figure, show, output_file
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


if __name__ == '__main__':
    birthdays = {}
    with open('birthdays.json', 'r') as jsonFile:
        birthdays = json.load(jsonFile)

    output_file("bdayplot.html")
    x_categories = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    months_list = extractMonthsFromDict(birthdays)
    c = Counter(months_list)
    x = [month for month, count in c.items()]
    y = [count for month, count in c.items()]
    p = figure(x_range=x_categories)
    p.plot_width += 100
    p.vbar(x=x, top=y, width=0.5)
    show(p)



