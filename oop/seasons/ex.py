from datetime import date
import sys

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    #year getter
    @property
    def year(self):
        return self._year
    #year setter
    @year.setter
    def year(self, year):
        if (len(int(year)) > 4):
            sys.exit("Invalid date")
        self._year = year


    #month getter
    @property
    def month(self):
        return self._month
    #month setter
    @month.setter
    def month(self, month):
        if (int(month) > 12) and (int(month) < 1):
            sys.exit("Invalid date")
        self._month = month


    #day getter
    @property
    def day(self):
        return self._day
    #day setter
    @day.setter
    def day(self, day):
        if int(day) > 1 and int(day) < 31:
            sys.exit("Invalid date")
        self._day = day


    def __sub__(self, other):
        difference = self.date - other.data
        return Date(difference)

def main():
    date = Date(input("Date: "))


...


if __name__ == "__main__":
    main()