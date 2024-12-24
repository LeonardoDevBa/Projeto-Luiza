from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
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

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

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

def senha1():
    while True:
        senha = str(pin.pwinput(f"{branco}Senha: {reset}"))
        senha1 = str(pin.pwinput(f"{cor}Digite a senha novamente: {reset}"))
        if senha and senha1:
            senha = criptografia(senha)
            break
        else:
            print(f"{cor}As senhas não são iguais, informe senhas iguais para prosseguir.{reset}")
    return senha

def verificar_funcionario(a):
    funcionario = repository.pesquisar_funcionario(a)
    return funcionario is not None

def verificar_garagem(a):
    funcionario = repository.pesquisar_garagem(a)
    return funcionario is not None

def verificar_item(a):
    funcionario = repository.pesquisar_item(a)
    return funcionario is not None

def criando_arquivo_final(caminho, dados):
    with open(caminho, "w") as arquivo:
        if isinstance(dados, list):
            for dado in dados:
                if isinstance(dado, bytes):
                    dado = dado.decode("utf-8")
                arquivo.write(dado)
        else:
            if isinstance(dados, bytes):
                dados = dados.decode("utf-8")
            arquivo.write(dados)
    print("\n=== Dados Salvos ===\n")

def lendo_arquivo_final(caminho):
    try:
        with open(caminho, "r") as arquivo:
            dados = arquivo.read()
            print("\n=== Dados Lidos ===\n")
            return dados
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
        return None
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        return None

