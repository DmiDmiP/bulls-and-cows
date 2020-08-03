# -*- coding: utf-8 -*-

from bulls_and_cows_engine import number_check, make_number, del_secret

count = 0
print('You need to guess the 4-digit number conceived by the computer.')
print('the computer guessed a number without repeating digits')

while count != 12:
    secret_number = make_number()
    user_num = input(f'{count+1} attempt. enter your number: ')
    if not user_num.isnumeric():
        print('This must be a four-digit number!')
    elif len(user_num) == 4:
        bull_cow = number_check(user_num)
        count += 1
    else:
        print('The number must be four digits!')
    print(f'among you: cows - {bull_cow["cow"]} bulls - {bull_cow["bull"]} .')
    if bull_cow['bull'] == 4:
        print(f'HOORAY! You have guessed {user_num} in {count} steps')
        one_more = input('want another batch y/n? ')
        if one_more == 'y':
            del_secret()
            count = 0
        else:
            break
    elif count == 12:
        print(f'you didn\'t guess the number {secret_number} in 12 steps.')
        one_more = input('want another batch y/n? ')
        if one_more == 'y':
            del_secret()
            count = 0
        else:
            break
