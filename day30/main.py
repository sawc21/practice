height = float(input("Height: "))
weight = float(input("Weight: "))


if height > 3:
    raise ValueError("Human Height should be less than 3 meters.")
bmi = weight / height ** 2
print(f"Your BMI is: {bmi}")