import pytest

from functions import *


def test_soma_1():
    assert soma_1(41) == 42


def test_soma_1_numero_com_string():
    assert soma_1("41") == 42


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1("fabio")


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1("fabio")
