import pandas

alpha_df = pandas.read_csv("supportfiles/nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index, row) in alpha_df.iterrows()}

request = input("What word would you like translated?").upper()
result = [alpha_dict.get(x) for x in request]
print(result)
