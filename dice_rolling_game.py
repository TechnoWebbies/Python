import random
counter = 0

while True:
    choice = input("Roll the Dice (y/n)? :").lower()

    if choice == "y":
        try:
            count = int(input("how many dice do you need? : "))
            if count < 1:
                print("Please enter valid number at least 1")
                continue

            rolls = [random.randint(0, 9) for _ in range(count)]
            print(f'Rolled: {tuple(rolls)}')
            counter += 1

        except ValueError:
            print("Invalid input please input valid input")

    elif choice == "n":
        print("Thanks for playing!")
        print(f'Rolls Count: {counter}')
        break

    else:
        print("Invalid Choice!!")
