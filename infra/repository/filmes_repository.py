# arquivo de interação SQL

from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def select_drama_films(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(
                    Filmes.genero == 'desconhecido').all()
                return data
            except NoResultFound:
                return None

    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                # rollback() - volta o db ao estado
                # o anterior caso tenha sido alterado
                raise exception

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, titulo, novo_titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(
                    Filmes.titulo == titulo).update(
                    {'titulo': novo_titulo, 'genero': genero, 'ano': ano})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception