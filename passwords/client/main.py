import sys
import string
import random

from src.ceasar.crypt import crypt


CEASAR_SHIFT = 2
CEASAR_ALPHA = string.ascii_letters

CEASAR_ENCODE_ALPHA = list(CEASAR_ALPHA)
random.shuffle(CEASAR_ENCODE_ALPHA)
CEASAR_ENCODE_ALPHA = ''.join(CEASAR_ENCODE_ALPHA)


class Account:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password


def run():
    load_ceaser_variables()
    action = sys.argv[1]

    if action == 'new':
        create_account()


def create_account():
    account = get_account()
    encode_account(account)
    save_account(account)


def get_account() -> Account:
    login = input('Enter login: ')
    password = input('Enter password: ')
    return Account(login=login, password=password)


def load_ceaser_variables():
    pass


def encode_account(account: Account) -> None:
    account.login = crypt(
        account.login,
        CEASAR_SHIFT,
        CEASAR_ALPHA,
        CEASAR_ENCODE_ALPHA
    )
    account.password = crypt(
        account.password,
        CEASAR_SHIFT,
        CEASAR_ALPHA,
        CEASAR_ENCODE_ALPHA
    )


def save_account(account: Account):
    with open('accounts', 'a') as f:
        f.write(f'{account.login},{account.password}\n')


if __name__ == '__main__':
    run()
