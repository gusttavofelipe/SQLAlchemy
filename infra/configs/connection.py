# arquivo de conexão com o db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://gustavo:root@localhost:3306/cinema'
        self.__engine = self.__create_db_engine()  # cria a engine
        self.session = None

    def __create_db_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):  # executado ao inicar calsse
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self  # retorna todos os objetos self da classe

    def __exit__(self, exc_type, exc_val, exc_tb):  # executado ao fechar calsse
        self.session.close()
