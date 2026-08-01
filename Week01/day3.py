age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")



num = int(input("Enter a number: "))
if num>0 :
    print("The number is positive")
elif num<0 :
    print("The number is negative")
else :
    print("The number is zero.")



s_age = int(input("Enter your age: "))
if s_age >= 18 and s_age <= 25 :
    print("You are eligible for the student discount.")
else :
    print("You are not eligible for the student discount.")



t_num = int(input("Enter a number: "))
if t_num%2==0 :
    print("The number is even.")
else :
    print("The number is odd.")



num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1==num2 :
    print("Both numbers are equal.")
else :
    if num1>num2 :
        print("The larger number is " + str(num1))
    else :
        print("The larger number is " + str(num2))