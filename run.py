from infra.repository.filmes_repository import FilmesRepository


repo = FilmesRepository()
repo.insert('Clube da luta', 'acao', 1999)
repo.update('Clube da luta', 'Blade' ,'a', 2049)
repo.delete('Blade')

data = repo.select()

print(data)
