print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = int((low + high) / 2)

user_inp = ''

while user_inp != 'c':
    print('Is your secret number ' + str(guess) + '?')
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if user_inp == 'h':
        high = guess
    elif user_inp == 'l':
        low = guess
    elif user_inp == 'c':
        print('Game over. Your secret number was:', guess)
        break
    else:
        print('Sorry, I did not understand your input.')
        continue

    guess = int((low + high) / 2)
