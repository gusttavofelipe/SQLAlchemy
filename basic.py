from sqlalchemy import create_engine, text


engine = create_engine('mysql+pymysql://gustavo:root@localhost:3306/cinema')
conn = engine.connect() # abre uma conexão com o db
response = conn.execute(text('SELECT * FROM filmes;')) 
# execute - executa instrução SQL, text - permite que a instrução em texto seja executada

for row in response:
    print(row)
    print(row.titulo)

# print(engine)