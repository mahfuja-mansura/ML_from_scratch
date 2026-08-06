def greet(name="Guest"):
    print("Hello, "+ name + "!" + "\nWelcome to Python!")
name = input("Enter your name: ")
greet(name)
greet()

print("--------------------")

def introduce(name, university):
    print("Hello, " + name + "!" + "\nYou study at " + university + ".")
name = input("Enter your name: ")
uni = input("Enter your university: ")
introduce(name, uni)

print("--------------------")

def add(a,b):
    return a+b
   
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
result = add(num1,num2)
print("The sum is :", result)

print("--------------------")

def check_even_odd(number):
    if number%2==0:
        return "The number is even"
    else:
        return "The number is odd"

num = int(input("Enter a number: "))
print(check_even_odd(num))

print("--------------------")

def subtract(a,b):
        return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
         return a/b

print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))
print(divide(10,5))
    