import random
hidden = random.randint(1,3)
guess = int(input('Enter the guess(number between 1 and 20): '))
while guess != hidden:
    print(guess, "is not corrct...")
    guess = int(input('Enter another number: '))
    if guess < hidden:
        print("the guess is too low")
    else:
        print("the guess is too high")
print(guess, "is corrct...")   
       
