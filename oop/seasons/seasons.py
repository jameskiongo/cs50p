from datetime import datetime
import sys

class Date:
    def __init__(self, date):
        self.date = date
    
    @classmethod
    def get(cls):
        while True:
            date = input("Date: ")
            try:
                format_date = "%Y-%m-%d"
                new_date = datetime.strptime(date, format_date)
                if new_date:
                    return cls(date)
                break
            except ValueError:
                sys.exit("Invalid date")
    def __sub__(self, other):
        difference = self.date - other.date
        return Date(difference)


def main():
    date = Date.get()
    current_date = datetime.today().date().strftime("%Y-%m-%d")
    difference = date - current_date
    print(difference)


# prompt user
# user input cannot be empty
# user input must be in YYYY-MM-DD
# def validate_date(date):
#     #yyyy-mm-dd
#     year, month, day = date.split("-")
    

if __name__ == "__main__":
    main()