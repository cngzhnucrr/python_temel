""" pythonda takvimi gsteren program yazma """

import calendar

year=int(input("yıl giriniz:"))
month=int(input("ay giriniz:"))

cal=calendar.month(year,month)
print(cal)