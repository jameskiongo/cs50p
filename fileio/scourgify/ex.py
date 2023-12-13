from tabulate import tabulate
import csv
import sys

def main():
    check_argv()
    data = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['first_name', 'last_name']
        for row in reader:
            full_name = row['name']
            house = row['house']
            last_name, first_name = full_name.split(', ')
            row['first_name'] = first_name
            row['last_name'] = last_name
            row['house'] = house
            data.append({'first_name': row['first_name'], 'last_name': row['last_name'], 'house': row['house']})
        print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a Python file")
        
if __name__ == "__main__":
    main()