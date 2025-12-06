import random

a = random.randint(0,100)
i = 0

while True:
    b = int(input("Enter the number within 0 to 100:"))
    i += 1
    if b == a:
        print("Congratulations! You guessed the correct number.")
        break
    elif b-a < 10:
        print("Your guess is too low. Try again!")
    elif b-a > 10:
        print("Your guess is too high. Try again!")
    else:
        print("Invalid input.")
    

print("The computer number was:",a)
print(f"Total attempts is {i}")

