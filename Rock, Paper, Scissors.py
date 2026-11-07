import random
choice = input('Choose from Rock/Paper/Scissors: ').lower()
random_n = random.randint(1,3)
if random_n == 1:
    print("The computer's choice is Rock")
elif random_n == 2:
    print("The computer's choice is Paper")
elif random_n == 3:
    print("The computer's choice is Scissors")
print('Your choice is',choice)
if random_n == 1 and choice == 'scissors':
    print('Rock beats Scissors! You lost!')
elif random_n == 1 and choice == 'paper':
    print('Paper beats Rock! You Won!')
elif random_n == 2 and choice == 'rock':
    print('Paper beats Rock! You lost!')
elif random_n == 2 and choice == 'scissors':
    print('Scissors beats Paper! You won!')
elif random_n == 3 and choice == 'rock':
    print('Rock beats Scissors! You won!')
elif random_n == 3 and choice == 'paper':
    print('Scissors beats Paper! You lost!')
elif random_n == 1 and choice == 'rock' or random_n == 2 and choice == 'paper' or random_n == 3 and choice == 'scissors':
    print('It is a draw!')