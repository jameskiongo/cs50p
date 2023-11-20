import random
import sys


def main():
    for time in range(2):
        generate_integer(get_level())
        calc = x + y
    # print(f"{x} + {y} = ", end = "")
    # ans = int(input(""))
    # if ans == calc:
    #     break
    # else:
    #     print("EEE")
    #     pass


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1 or n > 3: 
                pass
            else:
                break
        except ValueError:
            pass

def generate_integer(level):
    while True:
        try:
            x = random.randint(1,10)
            y = random.randint(1,10)
            return x, y
        except ValueError:
            print("EEE")
            pass


if __name__ == "__main__":
    main()