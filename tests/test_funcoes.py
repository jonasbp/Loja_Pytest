import pytest
from ..funcoes import *

# VERIFICA IDADE
@pytest.mark.usuario
def test_verifica_idade_grande():
    assert valida_idade(121) == False

@pytest.mark.usuario
def test_verifica_idade_zero():
    assert valida_idade(0) == True

@pytest.mark.usuario
def test_verifica_idade_120():
    assert valida_idade(120) == True

@pytest.mark.usuario
def test_verifica_idade_negativa():
    assert valida_idade(-1) == False

@pytest.mark.usuario
def test_verifica_idade_aleatoria_valida():
    assert valida_idade(22) == True

# VALIDA CPF
@pytest.mark.usuario
def test_verifica_cpf_valido():
    assert valida_cpf("11111111111") == True

@pytest.mark.usuario
def test_verifica_cpf_pequeno():
    assert valida_cpf("111") == False

@pytest.mark.usuario
def test_verifica_cpf_grande():
    assert valida_cpf("1111111111111111111111") == False

#VALIDA EMAIL
@pytest.mark.usuario
def test_verifica_email_valido():
    assert valida_email("jonas@jonas.com.br") == True

@pytest.mark.usuario
def test_verifica_email_invalido_sem_dominio():
    assert valida_email("jonas@") == False

@pytest.mark.usuario
def test_verifica_email_invalido_sem_nome():
    assert valida_email("@jonas.com.br") == False

#PRODUTO
#PREÇO
@pytest.mark.produto
def test_verifica_preco_invalido_negativo():
    assert valida_preco(-1) == False

@pytest.mark.produto
def test_verifica_preco_valido_zero():
    assert valida_preco(0) == True

@pytest.mark.produto
def test_verifica_preco_valido_aleatorio():
    assert valida_preco(10) == True

#ESTOQUE
@pytest.mark.produto
def test_verifica_estoque_invalido_negativo():
    assert valida_estoque(-1) == False

@pytest.mark.produto
def test_verifica_estoque_valido_zero():
    assert valida_estoque(0) == True

@pytest.mark.produto
def test_verifica_estoque_valido_aleatorio():
    assert valida_estoque(10) == True

#CATEGORIA
@pytest.mark.produto
def test_verifica_categoria_invalida():
    assert valida_categoria("Cachorro") == False

@pytest.mark.produto
def test_verifica_categoria_valida():
    assert valida_categoria("Limpeza") == True

#CLASSIFICAÇÃO
@pytest.mark.classificacao
def test_verifica_classificacao_invalida_usr():
    assert valida_classificacao(1,99) == False

@pytest.mark.classificacao
def test_verifica_classificacao_invalida_prod():
    assert valida_classificacao(99,1) == False

@pytest.mark.classificacao
def test_verifica_classificacao_valida():
    assert valida_classificacao(1,1) == True
