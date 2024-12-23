from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet
import pwinput as pin
from os import system

# Definindo cores
branco = "\033[97m"
cor = "\033[31m"  # Exemplo de cor vermelha
limpar = system("cls||clear")
reset = "\033[0m"  # Resetando para a cor padrão

# Configuração de sessão e inicialização
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
    senha = pin.pwinput(f"{branco}Senha: {reset}")  # Texto em branco
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

def descrição():
    descricao = input(f"{branco}: {reset}")
    funcionario = ... 
    data = datetime.now()
    dados = ("Data/Hora: ", data, "Descrição: ", descricao, "Funcionario: ", funcionario)

    dados_formatados = " ".join(map(str, dados))
    return dados_formatados

def cadastro_itens():
    while True:
        nome = input(f"{branco}Nome: {reset}")
        if verificar_item(nome):
            print(f"{cor}Erro, o item já existe.{reset}")
        else:
            break
    while True:
        quantidade = str(input(f"{branco}Quantidade: {reset}"))
        if quantidade.isnumeric:
            quantidade = int(quantidade)
            break
        else:
            print(f"{cor}Apenas números{reset}")

    descricao = descrição()
    
    service.criando_item(nome,quantidade,descricao)    

def cadastro_garagens():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        localizacao = str(input(f"{branco}Endereço: {reset}"))
        if verificar_garagem(localizacao):
            print(f"{cor}Erro! Garagem já cadastrada{reset}")
        else:
            break
    adicionais = descrição()

    service.criando_garagem(nome,localizacao,adicionais)

def senha1():
    while True:
        senha = input(f"{branco}Senha: {reset}")
        senha1 = input(f"{cor}Digite a senha novamente: {reset}")
        if senha == senha1:
            senha = criptografia(senha)
            break
        else:
            print(f"{cor}As senhas não são iguais, informe senhas iguais para prosseguir.{reset}")
    return senha

def cadastrando_funcionario():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        matricula = str(input(f"{branco}Matricula: {reset}")).strip()
        if matricula.isnumeric:
            matricula = str(matricula)
            if verificar_funcionario(matricula):
                print(f"{cor}Funcionario já cadastrado!{reset}")
            else:
                break
        else:
            print(f"{cor}Matricula inválida, digite apenas números!{reset}")
    senha = senha1()
    service.criando_funcionario(nome, matricula, senha)

def verificar_funcionario(a):
    funcionario = repository.pesquisar_funcionario(a)
    return funcionario is not None

def verificar_garagem(a):
    funcionario = repository.pesquisar_garagem(a)
    return funcionario is not None

def verificar_item(a):
    funcionario = repository.pesquisar_item(a)
    return funcionario is not None

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