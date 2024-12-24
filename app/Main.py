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
                limpar
                functions_app.menu_cadastro()
                opcao1 = input("0 - Sair\n: ").lower()
                match opcao1:
                    case '1':
                        functions_app.cadastrando_funcionario()
                    case "2":
                        functions_app.cadastro_garagens()
                    case "3":
                        functions_app.cadastro_itens()
                    case "0" |"sair":
                        break
                        
        case "2":
            functions_app.solicitacao()
        case "3":
            functions_app.historico()
        case "4":
            break