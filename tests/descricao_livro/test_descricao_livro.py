from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro("Pequenos Jangadeiros", "Aristides Fraga Lima", 96)
    assert (
        repr(livro)
        == f"O livro {livro.titulo} de {livro.autor} possui {livro.paginas} páginas."
    )
