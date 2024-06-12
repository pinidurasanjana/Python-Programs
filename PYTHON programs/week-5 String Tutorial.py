while True:
    secret = str("water")
    turns = 6
    guesses = " "
    print("Guess the Word")

    missed = 0
    guess = str(input("Enter the letter: "))
    guesses += guess

    for letter in secret:
        if letter in guesses:
            print('', letter, '', end='')
        else:
            print(' _ ', end='')
            missed += 1

    if guess not in secret:
        turns -= 1

    if missed == 0:
        print("Win")
        break
    
