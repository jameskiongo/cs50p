import sys

def main():
    check_argv()
    while True:
        try:
            new = open(sys.argv[1])
            new.readlines()
            new.close()
        except FileNotFoundError:
            sys.exit()

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    

if __name__ == "__main__":
    main()