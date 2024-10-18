import datetime
currentDate = datetime.date.today()

birthDate = input('Enter your birthday in YYYY/MM/DD format')
try:
    year, month, day = map(int, birthDate.split('/'))
    date1 = datetime.date(year, month, day)
except:
	print("input in the indicated format")
else:
	year, month, day = map(int, birthDate.split('/'))
	trueBirthDate = datetime.date(year, month, day)

Difference = currentDate - trueBirthDate
secondDifference = Difference.total_seconds()
dayDifference = int(divmod(secondDifference, 86400)[0])

checkValue = 10000

if dayDifference > checkValue:
    print("you are", str(dayDifference), "days old")
else:
	print("you will be 10000 days old in ", str(dayDifference - checkValue) , "days")