def main():
    import random
    import sys
    rocket = '>->'
    smoke = '-'
    n = 1
    i = 1
    wins = 0;
    # print("")
    # print("Total Wins: " + str(wins))
    print("")
    start_button = input("Press:\n0 to Exit\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division")

    if start_button == "0":
        sys.exit(0)
        print("Thank you for playing :) \nYou won " + wins + " times.")

    # Addition
    elif start_button == "1":
        while i <= 10:
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            print("What is " + str(a) + " + " + str(b) + "?")
            answer = int(input(">"))

            if int(a) + int(b) == answer:
                print("That answer is correct")
                print('')
                n = n + 1

                if n <= 10:
                    j = 1
                    j = j + 1
                    smoke = smoke * j
                    print(smoke + rocket)
                    print('')

                if n == 10:
                    print("The game is over! YOU WON!")
                    wins+1
                    main()
                    break
            else:
                print("")
                print("That is the wrong answer")
                main()

    # Subtraction
    elif start_button == "2":
        while i <= 10:
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            print("What is " + str(a) + " - " + str(b) + "?")
            answer = int(input(">"))

            if int(a) - int(b) == answer:
                print("That answer is correct")
                print('')
                n = n + 1

                if n <= 10:
                    j = 1
                    j = j + 1
                    smoke = smoke * j
                    print(smoke + rocket)
                    print('')

                if n == 10:
                    print("The game is over! YOU WON!")
                    wins+1
                    main()
                    break
            else:
                print("")
                print("That is the wrong answer")
                main()

    # Multiplication
    elif start_button == "3":
        while i <= 10:
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            print("What is " + str(a) + " * " + str(b) + "?")
            answer = int(input(">"))

            if int(a) * int(b) == answer:
                print("That answer is correct")
                print('')
                n = n + 1

                if n <= 10:
                    j = 1
                    j = j + 1
                    smoke = smoke * j
                    print(smoke + rocket)
                    print('')

                if n == 10:
                    print("The game is over! YOU WON!")
                    wins+1
                    main()
                    break
            else:
                print("")
                print("That is the wrong answer")
                main()

    # Division
    elif start_button == "4":
        while i <= 10:
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            print("What is " + str(a) + " / " + str(b) + "?")
            answer = int(input(">"))

            if int(a) / int(b) == answer:
                print("That answer is correct")
                print('')
                n = n + 1

                if n <= 10:
                    j = 1
                    j = j + 1
                    smoke = smoke * j
                    print(smoke + rocket)
                    print('')

                if n == 10:
                    print("The game is over! YOU WON!")
                    wins+1
                    main()
                    break
            else:
                print("")
                print("That is the wrong answer")
                main()


main()
