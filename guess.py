import random

number = random.randrange(1,50)
guess = int(input('guess a number between 1 and 50: '))
while guess != number:
	if guess < number:
		print('guess higher. Try again')
		guess = int(input('guess a number between 1 and 50: '))
	else:
		print('Guess lower. Try again')
		guess = int(input('guess a number between 1 and 50: '))
print('You guessed the number correctly')


