class Restaurante:
    def __init__(self, nome: str, pedidos: int = 0):
        if pedidos < 0:
            raise ValueError(
                "A quantidade de pedidos na fila deve ser maior ou igual a 0"
            )
        self.nome = nome
        self.pedidos_na_fila = pedidos

    def adiciona_pedido(self) -> None:
        self.pedidos_na_fila += 1

    def remove_pedido(self) -> None:
        self.pedidos_na_fila -= 1 if self.pedidos_na_fila > 0 else 0
