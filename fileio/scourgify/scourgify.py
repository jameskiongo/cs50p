import sys

def main():
    check_arg()
    
def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit(f"Could not read {sys.argv[1]}")
        
if __name__ == "__main__":
    main()
