"""
ID: saidhee1
LANG: PYTHON2
TASK: friday
"""

start_year = 1900
months_odd_days = {1:3,2:0,3:3,4:2,5:3,6:2,7:3,8:3,9:2,10:3,11:2,12:3}
years_odd_days = {100:5,200:3,300:1,400:0}
odd_days = {0:"sunday",1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
cache_year = {}

def check_leap_year(year):
    if year%100 == 0:
        if year%400 == 0:
            return 1
    elif year%4 == 0:
        return 1
    else:
        return 0

def get_odd_days_in_year(year):
    odd_days = 0
    if year == start_year-1:
        return 0
    if year in cache_year:
        return cache_year[year]
    temp = year % 400
    if temp/300 >= 1:
        odd_days += years_odd_days[300]
        temp = temp%300
    elif temp/200 >= 1 :
        odd_days += years_odd_days[200]
        temp = temp%200
    elif temp/100 >= 1:
        odd_days += years_odd_days[100]
        temp = temp%100
    if temp > 0:
        leap_years = temp/4
        non_leap_years = temp - leap_years
        odd_days += (leap_years * 2) + non_leap_years
    cache_year[year] = odd_days
    return odd_days

def get_odd_days_in_month(month,leap):
    odd_days = 0
    if month == 0:
        return 0
    for i in range(1,month+1):
        odd_days += months_odd_days[i]
    if month >= 2 and leap:
        odd_days += 1
    return odd_days

def get_odd_days(day,month,year):
    odd_days = 0
    leap = check_leap_year(year)
    odd_days += get_odd_days_in_year(year-1)
    odd_days += get_odd_days_in_month(month-1,leap)
    odd_days += day
    return odd_days%7

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
linelist = fin.readlines()

N = int(linelist[0])

print odd_days[get_odd_days(12,9,2018)]
frequencies = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
end_year = 1900 + N - 1
for year in range(1900,end_year+1):
    for month in range(1,13):
        day = get_odd_days(13,month,year)
        frequencies[day]+=1

fout.write(str(frequencies[6])+" ")
for i in range(5):
    fout.write(str(frequencies[i])+" ")
fout.write(str(frequencies[5])+"\n")
