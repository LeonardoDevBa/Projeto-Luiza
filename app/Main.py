from functions import functions_app
from os import system 
from time import sleep

limpar = ("cls||clear")

while True:
    functions_app.menu()
    opcao = input(": ")
    match opcao:
        case "1":
            limpar
            while True:
                functions_app.menu_cadastro()
                opcao1 = input(": ")
                match opcao1:
                    case '1':
                        functions_app.cadastrando_funcionario()
                    case "2":
                        functions_app.cadastro_garagens()
                    case "3":
                        functions_app.cadastro_itens()
        case "2":
            pass
        case "3":
            pass
        case "4":
            break