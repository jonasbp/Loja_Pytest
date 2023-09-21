import pytest
from .funcoes import *

@pytest.mark.usuario
def test_verifica_idade_grande():
    assert valida_idade(121) == False