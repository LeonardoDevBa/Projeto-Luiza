from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session

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