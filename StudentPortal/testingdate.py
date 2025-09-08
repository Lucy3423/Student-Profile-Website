import datetime

date = datetime.date.today()
# print(f"{date.day}/{date.month}/{date.year}")
day_name = date.strftime("%A") #A = full day (Monday), a = abbreviation (Mon)
print(day_name)

