############################# IMPORTS ##########################################
from sqlalchemy import create_engine, Column, String, Integer, Date, Sequence, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from login import login, senha
import cx_Oracle
################################################################################

# Cria a estrutura para conectar ao banco de dados que é passado no começo da string seguido pela biblioteca que auxilia nessa conexão

dnsStr = cx_Oracle.makedsn('fs-rac-scan', '1521', 'PDB')
dnsStr = dnsStr.replace('SID', 'SERVICE_NAME')

engine = create_engine(
    f'oracle+cx_oracle://{login}:{senha}@{dnsStr}')

# Cria a sessão de conexão com banco de dados (usuario deve conter permissões para essas interações)
Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# Instanciando a sessão de conexão
session = Session()

# pega as confiurações do sqlachemy no declaritive_base e joga dentro da variavel Base para ficar mais fácil
Base = declarative_base()


# Classe que vai herdar do declarative Base e vai criar as tabelas com os campos com cada caristica necessaria
'''class Falecidos(Base):
    meta = MetaData()
    __tablename__ = 'dw_falecidos_cwb'

    # Necessario para criar o autoincremente do Oracle
    id_seq = Sequence('id_seq', metadata=meta, order=True)
    id = Column(Integer, id_seq,  primary_key=True,)
    data_insercao = Column(String(250))
    nome = Column(String(250))
    data_do_falecimento = Column(Date)
    idade = Column(Integer)
    profissao = Column(String(250))
    nome_do_pai = Column(String(250))
    nome_da_mae = Column(String(250))
    conjuge = Column(String(250))
    numero_da_FAF = Column(String(250))
    local_do_falecimento = Column(String(250))
    local_do_velorio = Column(String(250))
    local_do_sepultamento = Column(String(250))
    data_do_sepultamento = Column(Date)
    funeraria = Column(String(250))

    # Representação do Objeto atraves do campo nome.
    def __repr__(self) -> str:
        return f'{self.nome}'''


class Falecidos_guar(Base):
    meta = MetaData()
    __tablename__ = 'falecidos'

    id_seq = Sequence('id_seq', metadata=meta, order=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_insercao = Column(String(250))
    nome = Column(String(250))
    idade = Column(Integer())
    nome_do_pai = Column(String(250))
    nome_da_mae = Column(String(250))
    data_do_falecimento = Column(Date)
    numero_da_faf = Column(Integer())
    cidade = Column(String(100))

    # Representação do Objeto atraves do campo nome.
    def __repr__(self) -> str:
        return f'{self.nome}'
