##############   datetime object   ###############
from datetime import datetime

current_date = datetime.now()
print(current_date)

# 1. Create a datetime obj for a specific date and time
create_date = datetime(2012,2,27,14,30,15)


#⃣ 2. Formatting a datetime Object using strftime():strftime("%Y-%m-%d %H:%M:%S %A %B")
formate_date = current_date.strftime("%A %B")
print(formate_date)