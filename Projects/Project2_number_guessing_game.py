secret_num = 7
test_num = int(input("Guess the number: "))
while test_num != secret_num:
    if test_num>secret_num:
        print("Too high!")
    else:
        print("Too low!")
    test_num = int(input("Guess the number: "))

print("Correct!")