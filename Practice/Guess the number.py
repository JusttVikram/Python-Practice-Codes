import random

target = random.randint(1,10)
print(target)

while True:
    user_choice = input('Guess the number or  Quit (Q): ')
    if user_choice == "Q":
        break
    user_choice = int(user_choice)
    if user_choice == target:
        print("You've guessed it right. Congratulations..!!")
        break
    elif user_choice < target:
        print("Try greater number.")
    else:
        print("Try smaller number.")

print("------ KAISA LAGA... MAZA AAYA KI NAI ------")



