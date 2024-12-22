from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from config.database import db

Base = declarative_base()
class Empresa(Base):
    __tablename__ = "empresas"

    nome = Column(String(100))
    cnpj = Column(String(14),primary_key = True)
    responsavel = Column(String(100))
    email = Column(String(100))
    senha = Column(String(100))

    usuarios = relationship("Usuario", back_populates="empresa", cascade="all, delete-orphan")
    
    def __init__(self,nome:str, cnpj:str, responsavel:str, email:str, senha:str):
        self.nome = nome
        self.cnpj = cnpj
        self.responsavel = responsavel
        self.email = email
        self.senha = senha

class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = Column(String(255), primary_key=True)
    nome = Column(String(100))
    sobrenome = Column(String(100))
    idade = Column(Integer)
    email = Column(String(100),primary_key=True)
    admissao = Column(DateTime)
    rg = Column(String(15))
    empresa_cnpj = Column(String(14), ForeignKey("empresas.cnpj"))

    empresa = relationship("Empresa", back_populates="usuarios")

    def __init__(self, cpf:str, nome: str,sobrenome: str, idade:int, email:str, admissao:DateTime,rg: str):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
        self.admissao = admissao
        self.rg = rg