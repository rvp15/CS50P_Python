##################### date object ####################
from datetime import date

# 1. datetime.date() class handles date objects without time. a part of datetime module

my_date = date(2025,2,27)   #date(Y,M,D) -> convert to 2025-02-27

# 2. Get today's date:
print(date.today())

# 3.To access date components
print(date.today().year)
print(date.today().month)

#4. Performing Date  (add days, seconds, microseconds, milliseconds, minutes, hours, and weeks with "timedelta") 
 # To perform onth and year, you have to use a library like dateutil.relativedelta from the dateutil module, which provides more flexible date arithmetic.
from datetime import timedelta

today = date.today()
after_30_days = today + timedelta(days=30)
print(after_30_days)