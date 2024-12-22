from models.usuario_model import Usuario, Empresa
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session:Session):
        
        self.session = session

    def salvar_usuario(self, usuario:Usuario):
        self.session.add(usuario)
        self.session.commit()

    def pesquisar_usuario(self, cpf: str):
        return self.session.query(Usuario).filter_by(cpf=cpf).first()
    
    def excluir_usuario(self, usuario:Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def atualizar_cadastro (self, usuario:Usuario):
        self.session.commit()
        self.session.refresh(usuario)
    
    def lista_usuarios(self):
        return self.session.query(Usuario).all()
    
    def pesquisar_empresa(self, cnpj: str):
        return self.session.query(Empresa).filter_by(cnpj = cnpj).first()