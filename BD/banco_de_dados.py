from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from BD.login import login, senha

engine = create_engine(f'mysql+pymysql://{login}:{senha}@localhost:3306/falecidos')

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine
)

session = Session()
Base = declarative_base()

class Falecidos(Base):
    __tablename__ = 'falecidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_insercao = Column(String(250))
    nome = Column(String(250))
    idade = Column(Integer())
    nome_do_pai = Column(String(250))
    nome_da_mae = Column(String(250))
    data_do_falecimento = Column(Date)
    numero_da_faf = Column(String(100))
    cidade = Column(String(100))

    def __repr__(self) -> str:
        return f'{self.nome}'