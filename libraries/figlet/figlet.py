import sys
import pyfiglet as pyg

if len(sys.argv) != 1 and len(sys.argv) != 2:
    sys.exit("Invalid usage")


if len(sys.argv) == 1:
    str = input("Input: ")
    out = pyg.figlet_format(str)
    print("Ouput: ")
    print(out)
elif len(sys.argv) == 2:
    if sys.argv[1] != "-f" or sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    else: 
        str = input("Input: ")
        
        out = pyg.figlet_format(str, font = sys.argv[1])
        print("Output: ")
        print(out)