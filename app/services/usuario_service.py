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

    # Criando Funcionario
    def criando_funcionario(self, nome: str, matricula: str, senha: str):
        try:
            # Validação da matrícula
            if len(matricula) != 4 or not matricula.isdigit():
                print(f"{cor}Matrícula inválida! A matrícula deve ter 4 dígitos numéricos.{reset}")
                sleep(3)
                return

            # Verificando se o funcionário já está cadastrado
            funcionario_cadastrado = self.repository.pesquisar_funcionario(matricula)
            if funcionario_cadastrado:
                print(f"{cor}Funcionário já cadastrado!{reset}")
                sleep(3)
                return

            # Criando o objeto Funcionario
            funcionario = Funcionario(nome=nome, matricula=matricula, senha=senha)

            # Salvando no banco de dados
            self.repository.salvar_funcionario(funcionario)
            print(f"{branco}Funcionário cadastrado com sucesso!{reset}")
            sleep(3)
        except TypeError as erro:
            print(f"{cor}Erro ao salvar o funcionário: {erro}{reset}")
            sleep(3)
        except Exception as erro:
            print(f"{cor}Ocorreu um erro inesperado: {erro}{reset}")
            sleep(3)

    # Criando Garagem
    def criando_garagem(self, nome: str, localizacao: str, adicionais: str):
        try:
            garagem_cadastrada = self.repository.pesquisar_garagem(localizacao)

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

    # Criando Itens (com verificação de permissão)
    def criando_item(self, nome: str, descricao: str, matricula_funcionario: str, localizacao_garagem: str):
        try:
            # Verificar permissão para criação de itens (usuário autorizado)
            if matricula_funcionario != "1234":  # Substitua pela matrícula do funcionário autorizado
                print("Você não tem permissão para criar itens!")
                sleep(3)
                return

            # Verificar se a garagem existe
            garagem = self.repository.pesquisar_garagem(localizacao_garagem)
            if not garagem:
                print("Garagem não encontrada!")
                sleep(3)
                return

            # Criar o item e associar à garagem
            item = Item(nome=nome, descricao=descricao, matricula_funcionario=matricula_funcionario, localizacao_garagem=localizacao_garagem)
            self.repository.salvar_item(item)
            print("Item criado com sucesso!")
            sleep(3)
        except TypeError as erro:
            print(f"Erro ao criar o item: {erro}")
            sleep(3)
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
            sleep(3)

    # Listar Funcionários
    def listar_funcionarios(self):
        try:
            funcionarios = self.repository.listar_funcionarios()
            return funcionarios
        except Exception as erro:
            print(f"Erro ao listar funcionários: {erro}")
            return []

    # Listar Itens
    def listar_itens(self):
        try:
            itens = self.repository.listar_itens()
            return itens
        except Exception as erro:
            print(f"Erro ao listar itens: {erro}")
            return []

    # Listar Garagens
    def listar_garagens(self):
        try:
            garagens = self.repository.listar_garagens()
            return garagens
        except Exception as erro:
            print(f"Erro ao listar garagens: {erro}")
            return []
