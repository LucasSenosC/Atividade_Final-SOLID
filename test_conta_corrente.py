import pytest
from ContaCorrente import ContaCorrente

@pytest.fixture
def conta_com_saldo_positivo():
    return ContaCorrente(id_conta="23456", saldo=10000.00, limite_da_conta=20000.00)

def test_depositar_valor_positivo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.depositar(valor_de_deposito=1000.00)
    assert conta_com_saldo_positivo.saldo == 11000.00

def test_depositar_valor_negativo(conta_com_saldo_positivo):
        with pytest.raises(ValueError, match="Valor de deposito inválido. Deve ser maior que zero."):
            conta_com_saldo_positivo.depositar(valor_de_deposito=-100.00)

def test_depositar_valor_usando_string(conta_com_saldo_positivo):
        with pytest.raises(TypeError, match="O valor do depósito deve ser do tipo float."):
            conta_com_saldo_positivo.depositar(valor_de_deposito="100.00")

def test_sacar_valor_positivo_dentro_do_limite_mais_saldo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.sacar(valor_de_saque=1000.00)
    assert conta_com_saldo_positivo.saldo == 9000.00

def test_sacar_valor_positivo_acima_do_limite_mais_saldo(conta_com_saldo_positivo):
    with pytest.raises(ValueError, match="Saldo insuficiente para realizar o saque."):
            conta_com_saldo_positivo.sacar(40000.00)

def test_sacar_valor_negativo(conta_com_saldo_positivo):
        with pytest.raises(ValueError, match="Valor de saque inválido. Deve ser maior que zero."):
            conta_com_saldo_positivo.sacar(-100.00)

def test_sacar_valor_usando_string(conta_com_saldo_positivo):
        with pytest.raises(TypeError, match="O valor do saque deve ser do tipo float."):
            conta_com_saldo_positivo.sacar("100.00")

def test_get_saldo(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_saldo() == 10000.00

def test_get_id_conta(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_id_conta() == "23456"

def test_get_limite_da_conta(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_limite_da_conta() == 20000.00

def test_set_saldo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_saldo(novo_saldo=50.00)
    assert conta_com_saldo_positivo.saldo == 50.00

def test_set_id_conta(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_id_conta(novo_id="11111")
    assert conta_com_saldo_positivo.id_conta == "11111"

def test_set_limite_da_conta_usando_valor_negativo(conta_com_saldo_positivo):
    with pytest.raises(ValueError, match="O novo limite deve ser não negativo."):
        conta_com_saldo_positivo.set_limite_da_conta(novo_limite=-30000.00)

def test_set_limite_da_conta_usando_float(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_limite_da_conta(novo_limite=30000.00)
    assert conta_com_saldo_positivo.limite_da_conta == 30000.00

def test_set_limite_da_conta_usando_str(conta_com_saldo_positivo):
    with pytest.raises(TypeError, match="O novo limite deve ser do tipo float."):
        conta_com_saldo_positivo.set_limite_da_conta(novo_limite="30000.00")


