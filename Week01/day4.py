for i in range(5):
    print(str(i+1))

print("--------------------")

for i in range(2,21,2):
    print(i)

print("--------------------")

num = int(input("Enter a number: "))
for i in range(1,11):
    
    print(num, " X ",i, " = ", num*i)

print("--------------------")

number = int(input("Enter a number: "))
total = 0
for i in range(1,(number+1)):
    total += i
    if i==number:
        print(i, " = ", end="")
    else:
        print(i, " + ", end="")

print(total)

print("--------------------")

count = 5
while count>0:
    print(count)
    count-=1

print("---------------------")

count = 1
while count<=10:
    if count==7:
        break
    print(count)
    count+=1

print("---------------------")

count = 0
while count<10:
    count+=1
    if count==5:
        continue
    print(count)

print("---------------------")

sign = "* "
for i in range(3):
    print(sign*4)

print("---------------------")

for i in range(5):
    for j in range(i+1):
        print("* ", end="")
    print()


