from models.usuario_model import Funcionario, Garagem, Item
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from time import sleep

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    # Criando Funcionario
    def criando_funcionario(self, matricula: str, nome: str, sobrenome: str, idade: int, email: str, admissao: datetime, rg: str):
        try:
            if len(matricula) != 4 or not matricula.isdigit():
                print("Matrícula inválida!")
                sleep(3)
                return

            funcionario = Funcionario(
                matricula=matricula, nome=nome, sobrenome=sobrenome, idade=idade,
                email=email, admissao=admissao, rg=rg
            )
            funcionario_cadastrado = self.repository.pesquisar_funcionario(funcionario.matricula)

            if funcionario_cadastrado:
                print("Funcionário já cadastrado!")
                sleep(3)
                return
            
            self.repository.salvar_usuario(funcionario)
            print("Funcionário cadastrado com sucesso")
            sleep(3)
        except TypeError as erro:
            print(f"Erro ao salvar o funcionário: {erro}")
            sleep(3)
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
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
            funcionarios = self.repository.lista_usuarios()
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
