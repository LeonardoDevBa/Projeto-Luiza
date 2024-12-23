from models.usuario_model import Funcionario, Garagem, Item
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from time import sleep
from os import system

branco = "\033[97m"
cor = "\033[31m"  
limpar = system("cls||clear")
reset = "\033[0m" 

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criando_funcionario(self, nome: str, matricula: str, senha: str):
        try:
            if len(matricula) != 4 or not matricula.isdigit():
                print(f"{cor}Matrícula inválida! A matrícula deve ter 4 dígitos numéricos.{reset}")
                sleep(3)
                return

            funcionario_cadastrado = self.repository.pesquisar_funcionario(matricula)
            if funcionario_cadastrado:
                print(f"{cor}Funcionário já cadastrado!{reset}")
                sleep(3)
                return

            funcionario = Funcionario(nome=nome, matricula=matricula, senha=senha)
            self.repository.salvar_funcionario(funcionario)
            print(f"{branco}Funcionário cadastrado com sucesso!{reset}")
            sleep(3)
        except Exception as erro:
            print(f"{cor}Erro ao salvar o funcionário: {erro}{reset}")
            sleep(3)

    def criando_garagem(self, nome: str, localizacao: str, adicionais: str):
        try:
            garagem_cadastrada = self.repository.pesquisar_garagem(nome)
            if garagem_cadastrada:
                print("Garagem já cadastrada!")
                sleep(3)
                return
            
            garagem = Garagem(nome=nome, localizacao=localizacao, adicionais=adicionais)
            self.repository.salvar_garagem(garagem)
            print("Garagem cadastrada com sucesso")
            sleep(3)
        except Exception as erro:
            print(f"Erro ao salvar a garagem: {erro}")
            sleep(3)

    def criando_item(self, nome: str, descricao: str, matricula_funcionario: str, localizacao_garagem: str, quantidade: float):
        try:
            if not isinstance(quantidade, (int, float)) or quantidade <= 0:
                print("Quantidade inválida! Insira um número positivo.")
                sleep(3)
                return

            funcionario = self.repository.pesquisar_funcionario(matricula_funcionario)
            if not funcionario:
                print("Funcionário não encontrado!")
                sleep(3)
                return

            garagem = self.repository.pesquisar_garagem(localizacao_garagem)
            if not garagem:
                print("Garagem não encontrada!")
                sleep(3)
                return

            item = Item(nome=nome, descricao=descricao, matricula_funcionario=matricula_funcionario, localizacao_garagem=localizacao_garagem, quantidade=quantidade)
            self.repository.salvar_item(item)
            print("Item criado com sucesso!")
            sleep(3)
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
            sleep(3)

    def listar_funcionarios(self):
        try:
            funcionarios = self.repository.listar_funcionarios()
            return funcionarios
        except Exception as erro:
            print(f"Erro ao listar funcionários: {erro}")
            return []

    def listar_itens(self):
        try:
            itens = self.repository.listar_itens()
            return itens
        except Exception as erro:
            print(f"Erro ao listar itens: {erro}")
            return []

    def listar_garagens(self):
        try:
            garagens = self.repository.listar_garagens()
            return garagens
        except Exception as erro:
            print(f"Erro ao listar garagens: {erro}")
            return []
