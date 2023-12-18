from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    birth_date = validate_date(input("Date: "))
    try:
        year, month, day = birth_date
    except:
        sys.exit("Invalid date")
    dob = date(int(year), int(month), int(day))
    today_date = date.today()
    diff = today_date - dob
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + "minutes")


def validate_date(date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        year,month,day = date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()