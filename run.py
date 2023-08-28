from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository

'''Atores'''

repo = AtoresRepository()
data = repo.select()
print(data)


print()

'''Filmes'''

repo2 = FilmesRepository()
data2 = repo2.select()
filme = data2[1]

print(filme.titulo) 
print(filme.atores)
# atores - atrbiuto de relação (relationship)

