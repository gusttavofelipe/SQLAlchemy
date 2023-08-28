# arquivo de entidades

from infra.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Filmes(Base):
    __tablename__ = 'filmes'
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Atores', backref='atores', lazy='subquery')
    # relationship - faz relacionamento entre suas classes

    def __repr__(self):
        return f'\n[Filme - {self.titulo}\n genero - {self.genero}\n ano - {self.ano}]\n'
