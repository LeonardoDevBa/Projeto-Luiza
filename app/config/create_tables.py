from config.database import db
from models.usuario_model import Funcionario, Garagem, Item
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_tables():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=db)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    create_tables()