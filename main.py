import pandas

nato_letters = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row["letter"]:row["code"] for (index, row) in nato_letters.iterrows()}

user_input = input("Input the word you want to convert to NATO alphabet: ")
user_input = user_input.upper()

output = [nato_alphabet[letter] for letter in user_input]
print(output)
