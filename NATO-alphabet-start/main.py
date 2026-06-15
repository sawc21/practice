

import pandas

phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")



phonetic_dict = {row.letter:row.code for (index,row) in phonetic_data_frame.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    try:
        word = input("Enter A word to be translated into phonetic code: ").upper()
        word_list = list(word)

        phonetic_list = [phonetic_dict[i] for i in word_list]
        print(phonetic_list)

    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
        
generate_phonetic()