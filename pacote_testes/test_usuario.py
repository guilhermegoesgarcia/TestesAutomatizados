from dominio import Usuario,Leilao
import pytest

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')
    vini.propoe_lance(leilao, 50.0)

    #esperamos que retorne:
    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_do_que_o_valor_da_carteira():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')
    vini.proproe_lance(leilao,1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_quando_o_lance_e_igual_valor_da_carteira():
    vini = Usuario('Vini',100.0)
    leilao = Leilao('Celular')
    vini.propoe_lance(leilao,100.0)

    assert vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_maior_que_contido_na_carteira():
    with pytest.raises(ValueError): # estamos esperando a exceção
        vini = Usuario('Vini',100.0)
        leilao = Leilao('Celular')
        vini.propoe_lance(leilao,200.0)


