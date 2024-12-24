from functions import functions_app
from os import system 
from time import sleep

def limpar():
    system("cls||clear")

while True:
    limpar()
    functions_app.menu()
    opcao = input(": ")
    match opcao:
        case "1":
            limpar()
            while True:
                limpar()
                functions_app.menu_cadastro()
                opcao1 = input("0 - Sair\n: ").lower()
                match opcao1:
                    case '1':
                        functions_app.cadastrando_funcionario()
                        sleep(2)
                    case "2":
                        functions_app.cadastro_garagens()
                        sleep(2)
                    case "3":
                        functions_app.cadastro_itens()
                        sleep(2)
                    case "0" |"sair":
                        limpar()
                        break  
        case "2":
            functions_app.solicitacao()
            sleep(3)
        case "3":
            functions_app.historico()
            sleep(3)
        case "4":
            break