import os
from getpass import getpass  # oculta os caracteres digitados no terminal


def header():
    print("****************************")
    print("***** Caixa Eletrônico *****")
    print("****************************")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def pause_terminal():
    os.system("pause")


def show_options(admin):
    print("1 - Saldo")
    if admin:
        print("10 - Inserir Cédulas")

    return input("Escolha uma das opções: ")


while True:
    header()

    account_typed = input("Digite o numero da conta: ")
    password_typed = getpass("Digite sua senha: ")

    account_list = {
        "101": {"password": "123", "name": "Helder", "value": 562, "admin": False},
        "102": {"password": "123", "name": "Santos", "value": 320, "admin": True},
    }

    if account_typed in account_list and password_typed == account_list[account_typed]["password"]:
        header()
        is_admin = account_list[account_typed]["admin"]

        option_typed = show_options(is_admin)
        if option_typed == "1":
            print("Seu saldo é: %s \n" % account_list[account_typed]["value"])
            pause_terminal()

    else:
        print("Conta inválida")

    clear_terminal()
