numbers = [10, 20, 30, 40, 50]
print(numbers)

print("--------------------")

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

print("--------------------")

fruits[0] = "Watermelon"
fruits[3] = "Pineapple"
print(fruits)

print("--------------------")

fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits.append("Pineapple")
fruits.append("Watermelon")
print(fruits)

print("--------------------")

fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
fruits.remove("Banana")
fruits.remove("Pineapple")
print(fruits)

print("--------------------")

fruits = ["Apple", "Mango", "Orange"]
fruits.insert(1, "Banana")
fruits.insert(3, "Pineapple")
print(fruits)

print("--------------------")

fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
fruits.pop(2)
fruits.pop()
print(fruits)

print("--------------------")

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

print("--------------------")

numbers = [3, 8, 12, 15, 21, 24, 30]
for num in numbers:
    if num>15:
        print(num)

print("--------------------")

numbers = [5, 10, 15, 20, 25]
total = 0
for num in numbers:
    total += num
print(total)

print("--------------------")

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
avg = total/len(numbers)
print(avg)

print("--------------------")

numbers = [45, 12, 89, 3, 67, 21]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print("--------------------")

grades = [75, 82, 91, 68, 88]
print("Grade List", grades, "\nThe number of Grades: ", len(grades), "\nTotal:", sum(grades), "\nAverage", (sum(grades)/len(grades)), "\nHighest Grade: ", max(grades), "\nLowest Grade: ", min(grades))

