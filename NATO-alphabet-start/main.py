# # student_dict = {
# #     "student": ["Angela", "James", "Lily"], 
# #     "score": [56, 76, 98]
# # }

# # #Looping through dictionaries:
# # for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:


phonetic_dict = {row.letter:row.code for (index,row) in phonetic_data_frame.iterrows()}

word = input("Enter A word to be translated into phonetic code: ").upper()

word_list = list(word)

#TODO 2. Create a list of the phonetic code words from a] word that the user inputs.wa
phonetic_list = [phonetic_dict[i] for i in word_list]
print(phonetic_list)

