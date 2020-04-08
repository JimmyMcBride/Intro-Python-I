# The Python standard library's 'calendar' module allows you to
# render a calendar to your terminal.
# https://docs.python.org/3.6/library/calendar.html
# 
# Write a program that accepts user input of the form
#   `14_cal.py month [year]`
# and does the following:
#  - If the user doesn't specify any input, your program should
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.
#  - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.
#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that
#    month and year.
#  - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.

import sys
from calendar import Calendar
from datetime import datetime

arg = sys.argv
todays_date = f"{datetime.today()}"
today = f"{todays_date[5]}{todays_date[6]}-{todays_date[8]}{todays_date[9]}-{todays_date[0]}{todays_date[1]}{todays_date[2]}{todays_date[3]}"
# print(today)

if len(sys.argv) > 3:
    print("please only enter (month year) as arguments")
else:
    month = sys.argv[1] if len(sys.argv) > 1 else datetime.now().month
    year = sys.argv[2] if len(sys.argv) > 2 else datetime.now().year
    
    calendar = Calendar()
    
    dates = calendar.itermonthdates(int(year), int(month))
    
    for date in dates:
        print(date)
