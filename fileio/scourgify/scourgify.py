from tabulate import tabulate
import csv
import sys

def main():
    check_arg()
    data = []
    try:
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
                data.append({'first': row['first_name'], 'last': row['last_name'], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
        
    with open(sys.argv[2], 'w') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)        
def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit(f"Could not read {sys.argv[1]}")
        
if __name__ == "__main__":
    main()
