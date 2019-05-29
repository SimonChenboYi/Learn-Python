guess_count = 0
guess_limit = 3
secrete_number = 9

while guess_count < guess_limit:
    guess = int(input('guess a number: '))
    guess_count += 1
    if guess == secrete_number:
        print('You Won!')
        break
else:
    print('You Failed!')
