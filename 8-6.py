from datetime import date

day_now = date.today()
print(day_now)

xday =  date(2005, 11, 12)
td = day_now - xday
print(td)
