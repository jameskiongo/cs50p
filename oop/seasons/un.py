from datetime import datetime
import inflect
import sys

p = inflect.engine()

def main():
    date = validate_date(input("Date: "))
    year, month, day = date.split("-")
    dob = (int(year), int(month), int(day))
    today = (2000, 1, 1)
    diff = today - dob
    diff = round(diff.total_seconds() / 60)
    output = p.number_to_words(diff, andword="")
    print(output.capitalize() + " minutes")


def validate_date(date):
    try:
        format_date = "%Y-%m-%d"
        valid_date = datetime.strptime(date, format_date)
        if valid_date:
            return valid_date
        else:
            sys.exit("Invalid Date")
    except ValueError:
        sys.exit("Invalid Date")
    

if __name__ == "__main__":
    main()