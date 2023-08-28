# arquivo de interação SQL

from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes


class AtoresRepository:
    def select(self):
        with DBConnectionHandler() as db:
            # consulta com relacionamentos
            data = db.session\
                .query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(Atores.nome, Filmes.genero, Filmes.titulo).all()
            return data
