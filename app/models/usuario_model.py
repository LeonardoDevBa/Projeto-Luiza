from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from config.database import db

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    nome = Column(String(100))
    matricula = Column(String(4), primary_key=True)
    senha = Column(String(100))

    garagens = relationship("Garagem", back_populates="funcionario", cascade="all, delete-orphan")
    itens = relationship("Item", back_populates="funcionario", cascade="all, delete-orphan")

    def __init__(self, nome: str, matricula: str, senha: str):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha


class Garagem(Base):
    __tablename__ = "garagens"

    nome = Column(String(25))
    localizacao = Column(String(255),primary_key=True)
    adicionais = Column(String(500))

    matricula = Column(String(4), ForeignKey("funcionarios.matricula"))

    funcionario = relationship("Funcionario", back_populates="garagens")
    itens = relationship("Item", back_populates="garagem", cascade="all, delete-orphan")

    def __init__(self, nome: str, localizacao: str, adicionais: str):
        self.nome = nome
        self.localizacao = localizacao
        self.adicionais = adicionais


class Item(Base):
    __tablename__ = "itens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    quantidade = Column(Float, nullable=False)

    matricula_funcionario = Column(String(4), ForeignKey("funcionarios.matricula"))
    localizacao_garagem = Column(String(255), ForeignKey("garagens.localizacao"))

    funcionario = relationship("Funcionario", back_populates="itens")
    garagem = relationship("Garagem", back_populates="itens")

    def __init__(self, nome: str, descricao: str, matricula_funcionario: str, localizacao_garagem: str, quantidade: float):
        self.nome = nome
        self.descricao = descricao
        self.matricula_funcionario = matricula_funcionario
        self.localizacao_garagem = localizacao_garagem
        self.quantidade = quantidade


Base.metadata.create_all(bind=db)
