##################### Extra Hard Starting Project ######################
import csv
import pandas as pd

birthday_file = "birthdays.csv"
# 1. Update the birthdays.csv

birthday_dataframe= pd.read_csv(birthday_file)
def save_birthday():
     return birthday_dataframe.to_csv(birthday_file, index=False)

def show_menu():
    selection = input(
        "Enter a selection:\n"
        "1) Update existing birthday\n"
        "2) Enter new birthday\n"
        "Selection: "
    )
    return selection

def get_birthday_info():
    name = input("Enter a name: ")
    email = input("Enter an email: ")
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))

    return {
        "name": name,
        "email": email,
        "year": year,
        "month": month,
        "day": day
    }

def add_birthday():
    return pd.concat([birthday_dataframe,
                                        pd.DataFrame([get_birthday_info()])],
                                        ignore_index=True
                            )


def update_birthday():
    print(birthday_dataframe)
    row_id = int(input("Enter a row id: "))
    updated_row = get_birthday_info()

    birthday_dataframe.loc[row_id, updated_row.keys()] = updated_row.values()
    return birthday_dataframe


def main():
    selection = show_menu()

    if selection == "1":
        update_birthday()
        save_birthday()
        print("birthday updated!")
    elif selection == "2":
        add_birthday()
        save_birthday()
        print("New birthday added!")

main()








# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




