from random import randint

secret_number = []


def make_number():
    global secret_number
    while not len(secret_number) == 4:
        random = randint(1, 9)
        while random not in secret_number:
            secret_number.append(random)
    return secret_number



def number_check(user_num):
    bull_cow = {'bull': 0, 'cow': 0}
    for count_secret, secret_item in enumerate(secret_number):
        for count_user , user_item in enumerate(user_num):
            if secret_item == int(user_item):
                if count_secret == count_user:
                    bull_cow['bull'] += 1
                else:
                    bull_cow['cow'] += 1
    return bull_cow


def del_secret():
    global secret_number
    secret_number.clear()

if __name__ == '__main__':
    make_number()
    secret_number = [1,7,2,3]
    number_check('1713')
