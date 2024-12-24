from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from functions import configuracoes_app
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


def descricao():
    descricao = input(f"{branco}Descrição: {reset}")
    data = datetime.now()
    dados = ("Data/Hora: ", data, "Descrição: ", descricao)
    dados_formatados = " ".join(map(str, dados))
    return dados_formatados

def cadastro_itens():
    while True:
        nome = input(f"{branco}Nome: {reset}")
        if configuracoes_app.verificar_item(nome):
            print(f"{cor}Erro, o item já existe.{reset}")
        else:
            break
    descricao_item = descricao()
    matricula = input(f"{branco}Matrícula do Funcionário: {reset}")
    while True:
        quantidade = input(f"{branco}Quantidade: {reset}")
        if quantidade.isnumeric():
            quantidade = int(quantidade)
            break
        else:
            print(f"{cor}Apenas números{reset}")
    localizacao_garagem = input(f"{branco}Localização da Garagem: {reset}")
    service.criando_item(nome, descricao_item, matricula, localizacao_garagem, quantidade)

def cadastro_garagens():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        localizacao = str(input(f"{branco}Endereço: {reset}"))
        if configuracoes_app.verificar_garagem(localizacao):
            print(f"{cor}Erro! Garagem já cadastrada{reset}")
        else:
            break
    adicionais = input("Dados Adicionais")

    service.criando_garagem(nome,localizacao,adicionais)

def cadastrando_funcionario():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        matricula = str(input(f"{branco}Matricula: {reset}")).strip()
        if matricula.isnumeric:
            matricula = str(matricula)
            if configuracoes_app.verificar_funcionario(matricula):
                print(f"{cor}Funcionario já cadastrado!{reset}")
            else:
                break
        else:
            print(f"{cor}Matricula inválida, digite apenas números!{reset}")
    senha = configuracoes_app.senha1()
    service.criando_funcionario(nome, matricula, senha)

def menu():
    print(f"""
{branco}1 - Cadastros 
2 - Solicitações
3 - Histórico de Movimentações
4 - Sair{reset}
""")
    
def menu_cadastro():
    print(f"""
{branco}1 - Funcionario
2 - Garagem
3 - Item{reset}
""")

def solicitacao_item():
    print("""
1 - Solicitar
2 - Sair
""")
    
def validacao_de_usuario():
    while True:
        matricula = str(input("Matrícula: ")).strip()
        if matricula.isnumeric():
            funcionario = repository.pesquisar_funcionario(matricula)
            if funcionario != None:
                break
        else:
            print("Matricula incorreta!")
    return funcionario

def login():
    funcionario = validacao_de_usuario()
    print(f"Seja bem vindo {funcionario.nome}")
    while True:
        senha = str(pin.pwinput("Senha:"))
        if senha == configuracoes_app.descriptografia(funcionario.senha):
            print("Login efetuado com sucesso")
            break
        else:
            print("Senha Incorreta!")  
    return funcionario

def solicitacao():
    funcinario = login()
    print("\n================= Itens =================")
    itens = service.listar_itens()
    for item in itens:
        print(f"ID: {item.id}   Nome: {item.nome}   QTD: {item.quantidade}  Garagem: {item.localizacao_garagem}")
    
    
def historico():
    dados_criptografados = configuracoes_app.lendo_arquivo_final("Historico.txt")
    if dados_criptografados:
        try:
            dados_descriptografados = configuracoes_app.descriptografia(dados_criptografados)
            print("=== Dados Descriptografados ===")
            print(dados_descriptografados)
        except ValueError as e:
            print(f"Erro na descriptografia: {e}")
    else:
        print("Nenhum dado foi encontrado ou erro ao ler o arquivo.")
    sleep(10)
