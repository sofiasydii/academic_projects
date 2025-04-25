### Dice rolling game

import random

while True:
    choice = input("Roll the dice? (yes/no) ").lower()
    if choice == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2} )")
    elif choice == 'no':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")

