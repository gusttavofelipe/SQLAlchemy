from sqlalchemy import (
    create_engine, text,
    Column, Integer, String
)
from sqlalchemy.orm import sessionmaker, declarative_base


# configurações
engine = create_engine(
    'mysql+pymysql://gustavo:root@localhost:3306/cinema'
)
Base = declarative_base()
# base declarativa - necessaria herdar na tabela

Session = sessionmaker(bind=engine)
# sessionmaker - cria uma sessão,
# bind vincula a sessão a engine, ao db

session = Session()  # obj de sessão


# entidades
class Filmes(Base):
    __tablename__ = 'filmes'  # nome da tabela relacionada
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'\n[Filme - {self.titulo}\n genero - {self.genero}\n ano - {self.ano}]\n'


# SQL:
# insert
data_insert = Filmes(
    titulo='Butterfly effect', genero='Fic cientifica', ano=2004
)
session.add(data_insert)
session.commit()

# delete
data_delete = session.query(Filmes).filter(
    Filmes.titulo == 'Contato').delete()
session.commit()

# update
data_update = session.query(Filmes).filter(
    Filmes.genero == 'Fic cientifica').update({'ano': 2049})
session.commit()

# select
data_select = session.query(Filmes).all()
print(data_select)
# print(data[0].titulo)  # possivel utilizar indices

session.close()
