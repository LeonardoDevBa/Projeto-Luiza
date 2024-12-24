from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
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
    return texto_criptografado.decode("utf-8")

def descriptografia(texto):
    if texto is None:
        raise ValueError("Texto criptografado não pode ser None!")
    if not isinstance(texto, str):
        raise ValueError(f"A entrada para descriptografia deve ser uma string! Entrada recebida: {type(texto)}")
    try:
        texto_criptografado = texto.encode("utf-8")  # Converte de volta para bytes
        texto_descriptografado = cipher.decrypt(texto_criptografado).decode("utf-8")
        return texto_descriptografado
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
    with open(caminho, "a") as arquivo:
        if isinstance(dados, list):
            for dado in dados:
                if not isinstance(dado, str):
                    raise ValueError(f"Dado inválido para criptografia: {dado}")
                criptografado = criptografia(dado)
                arquivo.write(f"{criptografado}\n")  # Cada linha é uma entrada criptografada
        else:
            if not isinstance(dados, str):
                raise ValueError(f"Dado inválido para criptografia: {dados}")
            criptografado = criptografia(dados)
            arquivo.write(f"{criptografado}\n")  # Escreve a string criptografada
    print("\n=== Dados Salvos ===\n")

def lendo_arquivo_final(caminho):
    try:
        with open(caminho, "r") as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            print("\n=== Dados Lidos ===\n")
            descriptografados = []
            for linha in linhas:
                linha = linha.strip()  # Remove espaços em branco e quebras de linha
                if linha:  # Verifica se a linha não está vazia
                    if not isinstance(linha, str):
                        raise ValueError(f"Linha inesperada para descriptografia: {linha}")
                    descriptografados.append(descriptografia(linha))  # Descriptografa a linha
            return descriptografados
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
        return None
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        return None
