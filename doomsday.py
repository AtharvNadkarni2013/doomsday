from datetime import datetime as d

# Variable Section

dayAnchors = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}
centuryAnchors = {18:5, 19:3, 20:2, 21:0}
listOfDaysCommon = {1:3, 2:28, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
listOfDaysLeap = {1:4, 2:29, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}



# Function Section

def getYearAnchor(year):
    century = year // 100
    last = year % 100
    if last % 2 == 0:
        last //= 2
        if last % 2 == 0:
            pass
        else:
            last += 11
    else:
        last += 11
        last //= 2
        if last % 2 == 0:
            pass
        else:
            last += 11
    last = 7 - (last % 7)
    return (last + centuryAnchors[century]) % 7

def getDayAnchor(year, month, day):
    days = list(dayAnchors.keys())
    yearAnchor = getYearAnchor(year)
    doom = listOfDaysLeap[month] if year % 4 == 0 else listOfDaysCommon[month]
    return days[(yearAnchor + ((day - doom) % 7)) % 7]

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
ymd = d(year, month, day).strftime("%B %d, %Y")
print(ymd, "was on a", getDayAnchor(year, month, day))