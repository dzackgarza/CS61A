import sys
chances = 0

while (chances < 3):
    try:
        try:
            submission = int(input("Enter a number between 1 and 10: "))
        except ValueError as e:
            raise ValueError("Input was not an integer, please try again.")

        if submission > 10:
            print("Too high.")
            raise ValueError("Input was too high.")
        elif submission < 1:
            raise ValueError("Input was too low.")
        else:
            print("Success! Number was " + str(submission))
            break

    except ValueError as e:
        print(e)
        chances += 1

        if chances < 3:
            print("Please try again.")
            print(str(3 - chances) + " more chances left.")
            continue
        else:
            print("Sorry, all chances used.")
            sys.exit(0)
