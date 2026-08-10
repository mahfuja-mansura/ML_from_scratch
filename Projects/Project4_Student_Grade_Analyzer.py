grades = []

for i in range(5):
    grades.append(int(input("Enter grade "+ str(i+1) + ": ")))

print("Grades: ", grades)
print("Number of grades: ", len(grades))
print("Total: ", sum(grades))
print("Average: ", sum(grades)/len(grades))
print("Highest: ", max(grades))
print("Lowest: ", min(grades))