student = {}

name = input("Enter your name: ")
age = int(input("Enter your age: "))
uni = input("Enter Your University name: ")
major = input("Enter your Major: ")
student["Name"] = name
student["Age"] = age 
student["University"] = uni
student["Major"] = major 
student["grades"] = [85,92,78,90,88]

for key, value in student.items():
    print(key, " : ", value)

print("Name: ", student["name"])
print("Grades: ",student["grades"])
print("Total: ", sum(student["grades"]))
print("Average", (sum(student["grades"])/len(student["grades"])))
print("Highest: ", max(student["grades"]))
print("Lowest: ", min(student["grades"]))