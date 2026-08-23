numbers = []
for i in range(1,6):
    numbers.append(int(input(f"Enter number {i}:")))

print("Original: ", numbers)

uniqueNum = set(numbers)

print("Unique: ",uniqueNum)