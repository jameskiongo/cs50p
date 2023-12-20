from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date: ").split("-")
        validate(year,month,day)
    except ValueError:
        sys.exit("Invalid Date")
    print(minutes(year,month,day))

def minutes(year,month,day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"
    tday = date.today()
    diff = tday - dt
    minutes = int(diff.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()
    

def validate(year, month, day):
    if not re.search(r"^\d{4}$", year):
        return "Invalid Date"
    if int(month) > 12 or int(month) < 1:
        return "Invalid Date"
    if int(day) > 31 or int(day) < 1:
        return "Invalid date"

    
if __name__ == "__main__":
    main()