def add(a,b):
    return a+b

def subtract(a,b):
        return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
         if b==0:
               return "Cannot divide by zero"
         return a/b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation: " + "\n1. Addition" + "\n2. Subtraction" + "\n3. Multiplication" + "\n4. Division")
choice = int(input("Enter Your Choice: "))

if choice==1:
      print("Result: ", add(num1,num2))
elif choice==2:
      print("Result: ", subtract(num1,num2))
elif choice==3:
      print("Result: ", multiply(num1,num2))
elif choice==4:
      print("Result: ", divide(num1,num2))
else:
      print("Invalid Choice")