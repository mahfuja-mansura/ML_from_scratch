weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight/(height**2)
bmi = round(bmi, 1)

if bmi < 18.5 :
    category = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9 :
    category = "Normal weight"
elif bmi >= 25 and bmi <= 29.9 :
    category = "Overweight"
else :
    category = "Obesity"

print("Your BMI is: " + str(bmi) + "\nCategory: " + category)
