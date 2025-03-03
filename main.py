#TODO 1. Create a dictionary in this format:
import pandas as pd
Data = pd.read_csv("nato_phonetic_alphabet.csv")
Data_dict = {row.letter:row.code for (index,row) in Data.iterrows()}
#print(Data_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_dict = [Data_dict[l] for l in word]
print(word_dict)

