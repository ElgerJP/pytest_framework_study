import pytest

from restaurante import Restaurante


@pytest.fixture
def restaurante_fila_vazia():
    return Restaurante("Pizza X")


@pytest.fixture
def restaurante_com_um_pedido():
    return Restaurante("Pizza X", 1)


@pytest.mark.parametrize("initial, final", [(0, 0), (1, 0), (2, 1)])
def test_remocao_de_pedidos(initial, final):
    restaurante = Restaurante("Pizza X", initial)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == final


def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero(restaurante_fila_vazia):
    assert restaurante_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero(restaurante_com_um_pedido):
    assert restaurante_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante("Pizza X", -1)


def test_adiciona_um_pedido_na_fila(restaurante_com_um_pedido):
    restaurante_com_um_pedido.adiciona_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 2


def test_adiciona_um_pedido_na_fila(restaurante_com_um_pedido):
    restaurante_com_um_pedido.remove_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 0


def test_adiciona_um_pedido_na_fila_vazia(restaurante_fila_vazia):
    restaurante_fila_vazia.remove_pedido()
    assert restaurante_fila_vazia.pedidos_na_fila == 0
