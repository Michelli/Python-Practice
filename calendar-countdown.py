from datetime import date
from datetime import datetime

event_date = datetime(2020,12,25,0,0) # Year/Month/Day/Hour/Minute

def date_calc(event):
    now = datetime.now()
    return (event - now).days

date_result = date_calc(event_date)

if date_result == 1:
    print(f"Nog {date_result} dag te gaan!")
elif date_result > 0:
    print(f"Nog {date_result} dagen te gaan!")
else:
    print("Het is al voorbij!")