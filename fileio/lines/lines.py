import sys

def main():
    check_argv()
    while True:
        try:
            with open(sys.argv[1]) as file:
                count = 0
                for line in file: 
                    if line[0] == "#":
                        None
                    elif line[0] == " ":
                        None
                    else:
                        count += 1
                print(count)
                break
        except FileNotFoundError:
            sys.exit("")

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    

if __name__ == "__main__":
    main()