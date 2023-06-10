print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = int((low + high) / 2.0)
guessed_correctly = False
while not guessed_correctly:
    print('Is your secret number ' + str(guess) + '?')
    user_reply = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_reply.lower() == 'c':
        guessed_correctly = True
        break
    elif user_reply.lower() == 'h':
        high = guess
    elif user_reply.lower() == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
        continue
    guess = int((low + high) / 2.0)
print('Game over. Your secret number was: ', guess)



