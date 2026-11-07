import random
ran_n = random.randint(100,999)
for i in range(1,4):
    guess = int(input('Enter the secret password made of only digits from 100 to 999: '))
    if guess == ran_n:
        print('Correct guess! The number was',ran_n)
        break
    else:
        if i == 1:
            if ran_n%2 == 0:
                print('The secret password is an even number!')
            elif ran_n%2 != 0:
                print('The secret password is an odd number!')
        if i == 2:
            if ran_n < 500:
                print('The secret password is less than 500!')
            elif ran_n >= 500:
                print('The secret code is either equal to or greater than 500!')
        if i == 3:
            print('Uh Oh! You lose! The secret password was',ran_n)
