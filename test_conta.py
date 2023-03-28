import pytest
from Conta import Conta

@pytest.fixture
def conta_com_saldo_positivo():
    return Conta(id_conta="23456", saldo=10000.00)

def test_depositar(conta_com_saldo_positivo):
    conta_com_saldo_positivo.depositar(valor_de_deposito=1000.00)
    assert conta_com_saldo_positivo.saldo == 10000.00

def test_sacar(conta_com_saldo_positivo):
    conta_com_saldo_positivo.sacar(valor_do_saque=1000.00)
    assert conta_com_saldo_positivo.saldo == 10000.00

def test_get_saldo(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_saldo() == 10000.00

def test_get_id_conta(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_id_conta() == "23456"

def test_set_saldo_usando_int(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_saldo(novo_saldo=50.00)
    assert conta_com_saldo_positivo.saldo == 50.00

def test_set_saldo_usando_string(conta_com_saldo_positivo):
    with pytest.raises(TypeError, match="O novo saldo deve ser do tipo float."):
        conta_com_saldo_positivo.set_saldo(novo_saldo="50.00")

def test_set_id_conta_usando_int(conta_com_saldo_positivo):
    with pytest.raises(TypeError, match="O novo id deve ser do tipo string."):
        conta_com_saldo_positivo.set_id_conta(novo_id=11111)

def test_set_id_conta_usando_string(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_id_conta(novo_id="11111")
    assert conta_com_saldo_positivo.id_conta == "11111"


