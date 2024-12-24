from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from functions import functions_app
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet
import pwinput as pin
from os import system
from time import sleep

branco = "\033[97m"
cor = "\033[31m"
limpar = system("cls||clear")
reset = "\033[0m"

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def inicialização():
    print("=== INICIALIZANDO SISTEMA ===")
    matricula = str(input("\nMatricula: "))
    funcionario = repository.pesquisar_funcionario(matricula)
    if funcionario.matricula and matricula.isnumeric():
        senha = str(input("Senha: "))
        if senha and funcionario.senha:
            limpar
            while True:
                print("===LOGIN EFETUADO===")
                functions_app.menu()
                opcao = str(input(": "))
                match opcao:
                    case "1":
                        while True:
                            functions_app.menu_cadastro()
                            sub_opcao = str(input(": "))
                            match sub_opcao:
                                case "1":
                                    functions_app.cadastrando_funcionario()
                                    sleep(2)
                                case "2":
                                    functions_app.cadastro_garagens()
                                    sleep(2)
                                case "3":
                                    functions_app.cadastro_itens()
                                    sleep(2)
                                case "_":
                                    print("Opção invalida!")
                                    sleep(2)    
                    case "2":
                        functions_app.solicitacao_item()
                    case "3":
                        functions_app.historico()
                    case "_":
                        break
        else:
            print("Senha incorreta!")                
    else:
        print("Erro na matricula!")