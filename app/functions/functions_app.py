from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet
import pwinput as pin
from os import system

cor = "\033[31m"
limpar=system("cls||clear")

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

def senha():
    senha = pin.pwinput("Senha: ")
    senha_seg = criptografia(senha)
    return senha_seg

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave


def criptografia(texto):
    texto_criptografado = cipher.encrypt(texto.encode("utf-8"))
    return texto_criptografado

def descriptografia(texto):
    if texto is None:
        raise ValueError("Senha não pode ser None!")
    if isinstance(texto, str):
        texto = texto.encode("utf-8")
    try:
        return cipher.decrypt(texto).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Erro na descriptografia: {e}")
    
def descrição ():
    descrição = input(": ")
    funcionario = ...
    data = datetime()
    dados = ("Data/Hora: ",data,"Descrição: ",descrição,"Funcionario: ",funcionario)
    return dados  

def cadastro_itens():
    while True:
        nome = input("Nome: ")
        if verificar_item(nome):
            print(f"{cor}Erro, o item já existe.")
        else:
            break
    while True:
        quantidade = str(input("Quantidade: "))
        if quantidade.isnumeric:
            quantidade = int(quantidade)
            break
        else:
            print("Apenas numeros")

    descricao = descrição()
    
    service.criando_item(nome,quantidade,descricao)    

def cadastro_garagens():
    nome = str(input("Nome: "))
    while True:
        localizacao = str(input("Endereço: "))
        if verificar_garagem(localizacao):
            print(f"{cor}Erro! Garagem já cadastrada")
        else:
            break
    adicionais = descrição()

    service.criando_garagem(nome,localizacao,adicionais)

def senha1 ():
    while True:
        senha = input("Senha: ")
        senha1 = input(f"{cor}Digite a senha novamente: ")
        if senha == senha1:
            senha = criptografia(senha)
            break
        else:
            print(f"{cor}As senhas não são iguais, informe senhas iguais para prosseguir.")
    return senha

def cadastrando_funcionario():
    nome = str(input("Nome: "))
    while True:
        matricula = str(input("Matricula: ")).strip()
        if matricula.isnumeric:
            matricula=str(matricula)
            if verificar_funcionario(matricula):
                print(f"{cor}Funcionario já cadastrado!")
            else:
                break
        else:
            print(f"{cor}Matricula inválida, digite apenas numeros!")
    senha = senha1()
    service.criando_funcionario(nome,matricula,senha)

def verificar_funcionario(a):
    funcionario = repository.pesquisar_funcionario(a)
    return funcionario is not None

def verificar_garagem(a):
    funcionario = repository.pesquisar_garagem(a)
    return funcionario is not None

def verificar_item(a):
    funcionario = repository.pesquisar_item(a)
    return funcionario is not None

def menu ():
    print("""
1 - Cadastros 
2 - Solicitações
3 - Historico de movimentações
4 - Sair
""")
    
def menu_cadastro():
    print("""
1 - Funcionario
2 - Garagem
3 - Item
          """)