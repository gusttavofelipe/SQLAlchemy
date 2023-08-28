# arquivo de entidades

from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Atores(Base):
    __tablename__ = 'atores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))
    # relação entre tabelas, ForeignKey -
    # nome da tabela relacionada+.+nome coluna coluna relacionada

    def __repr__(self):
        return f'\nAtores:\n[Nome -> {self.nome} | Fime -> {self.titulo_filme}]\n'
