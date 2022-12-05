import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

dictionary = {i.letter: i.code for (index, i) in df.iterrows()}
print(dictionary)

name = input("Enter Name : ").upper()

nato_list = [dictionary[letter] for letter in name]

for i in nato_list:
    print(i[0], "for", i)
