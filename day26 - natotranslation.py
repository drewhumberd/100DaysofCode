import pandas

alpha_df = pandas.read_csv("supportfiles/nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index, row) in alpha_df.iterrows()}

def phonetic():
    request = input("What word would you like translated?").upper()
    try:
        result = [alpha_dict[x] for x in request]
    except KeyError:
        print("Sorry, only alphabetic characters allowed.")
        phonetic()
    else:
        print(result)

phonetic()
