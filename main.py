import pandas

nato_letters = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row["letter"]:row["code"] for (index, row) in nato_letters.iterrows()}

correct_input = False
while not correct_input:
    user_input = input("Input the word you want to convert to NATO alphabet: ")
    user_input = user_input.upper()
    try:
        output = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Use only letters in English the alphabet!\n")
    else:
        correct_input = True


print(output)
