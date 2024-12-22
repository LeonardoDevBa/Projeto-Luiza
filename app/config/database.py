from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "adm"
db_password = "adm123"
db_name = "banco"
db_host = "localhost"
db_port = "3306"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db = create_engine(DATABASE_URL)

Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as erro:
        db.rollback()
        raise erro
    finally:
        db.close()
        