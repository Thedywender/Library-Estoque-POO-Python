from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("Antropologia", "Maria Aparecida Lopes", 292)
    assert livro.titulo == "Antropologia"
    assert livro.autor == "Maria Aparecida Lopes"
    assert livro.paginas == 292
