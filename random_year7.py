from random import randint as ri


N = ri(0,10)

chances = 7

while chances > 0:
    guess = int(input('Give your guess: '))
    chances -= 1 # chances = chances - 1
    if guess == N:
        print(f'😻 You won! The number was {N}')
        break
    else:
        if guess < N:
            print('Too low. Try again.')
        elif guess > N:
            print('Too high. Try again.')
        if chances == 0:
            print(f"You didn't get it right in time. The correct answer is {N}")
            break
        print(f'You have {chances} chances!')
    
    