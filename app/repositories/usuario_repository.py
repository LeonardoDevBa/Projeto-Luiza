from models.usuario_model import Funcionario, Garagem, Item
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    # Métodos para Funcionario
    def salvar_funcionario(self, funcionario: Funcionario):
        self.session.add(funcionario)
        self.session.commit()

    def pesquisar_funcionario(self, matricula: str):
        return self.session.query(Funcionario).filter_by(matricula=matricula).first()

    def excluir_funcionario(self, funcionario: Funcionario):
        self.session.delete(funcionario)
        self.session.commit()

    def atualizar_cadastro_funcionario(self, funcionario: Funcionario):
        self.session.commit()
        self.session.refresh(funcionario)

    def listar_funcionarios(self):
        return self.session.query(Funcionario).all()

    # Métodos para Garagem
    def salvar_garagem(self, garagem: Garagem):
        self.session.add(garagem)
        self.session.commit()

    def pesquisar_garagem(self, localizacao: str):
        return self.session.query(Garagem).filter_by(localizacao=localizacao).first()

    def excluir_garagem(self, garagem: Garagem):
        self.session.delete(garagem)
        self.session.commit()

    def listar_garagens(self):
        return self.session.query(Garagem).all()

    # Métodos para Item
    def salvar_item(self, item: Item):
        self.session.add(item)
        self.session.commit()

    def pesquisar_item_id(self, item_id: int):
        return self.session.query(Item).filter_by(id=item_id).first()

    def pesquisar_item_nome(self, nome_item:str):
        return self.session.query(Item).filter_by(nome=nome_item).first()


    def excluir_item(self, item: Item):
        self.session.delete(item)
        self.session.commit()

    def listar_itens(self):
        return self.session.query(Item).all()
