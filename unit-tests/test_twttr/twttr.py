def main():
    name = input("Input: ")
    n_name = shorten(name)
    print(n_name)
def shorten(word):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    #loop through word
    n_word = word
    for vowel in vowels:
        n_word = n_word.replace(vowel, "")
    #remove vowels
    return n_word
if __name__ == "__main__":
    main()