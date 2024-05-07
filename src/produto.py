class Produto:
    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco <= 0:
            raise ValueError("O preço deve ser um valor maior que zero!")
        self.__preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("a quantidade deve ser maior que zero!")
        self.__quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser mairo que zero")
        if quantidade > self.__quantidade:
            raise ValueError("Quantidade superior ao estoque")
        self.__quantidade -= quantidade
