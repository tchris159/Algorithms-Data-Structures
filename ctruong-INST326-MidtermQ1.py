import random
guessesTaken = 0
number = random.randint(1, 100)  #ranomize numbers
print('There is a number between 1 and 100, please try to guess it and i will give hints along the way.')
while(True):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1        #counter for number of guesses which is displayed at end
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break            #breaks out of code because they won/guessed correctly
    else:
        print('Error. Please enter a number in the range 1 to 100.')   #bad user/error if they input a guess beyond the range
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Amazing. ' + 'You guessed the number from 1-100 in ' + guessesTaken + ' guesses. Please play again!')

