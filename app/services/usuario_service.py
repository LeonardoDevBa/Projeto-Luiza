from models.usuario_model import Usuario, Empresa
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from time import sleep

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criando_empresa(self, nome: str, cnpj: str, responsavel: str, email: str, senha: str):
        try:
            if len(cnpj) != 14 or not cnpj.isdigit():
                print("CNPJ inválido!")
                sleep(3)
                return
            
            empresa = Empresa(nome=nome, cnpj=cnpj, responsavel=responsavel, email=email, senha=senha)
            empresa_cadastrada = self.repository.pesquisar_usuario(empresa.cnpj)

            if empresa_cadastrada:
                print("Empresa já cadastrada!")
                sleep(3)
                return
            
            self.repository.salvar_usuario(empresa)
            print("Empresa cadastrada com sucesso")
            sleep(3)
        except TypeError as erro:
            print(f"Erro ao salvar a empresa: {erro}")
            sleep(3)
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
            sleep(3)

    def criando_usuario(self, cpf: str, nome: str, sobrenome: str, idade: int, email: str, admissao: datetime, rg: str, empresa_cnpj = str):
        try:
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido!")
                sleep(3)
                return

            usuario = Usuario(
                cpf=cpf, nome=nome, sobrenome=sobrenome, idade=idade,
                email=email, admissao=admissao, rg = rg, empresa_cnpj = empresa_cnpj
            )
            usuario_cadastrado = self.repository.pesquisar_usuario(usuario.cpf)

            if usuario_cadastrado:
                print("Usuário já cadastrado!")
                sleep(3)
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso")
            sleep(3)
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
            sleep(3)
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
            sleep(3)

    def listar_usuarios(self):
        try:
            usuarios = self.repository.lista_usuarios()
            return usuarios
        except Exception as erro:
            print(f"Erro ao listar usuários: {erro}")
            return []