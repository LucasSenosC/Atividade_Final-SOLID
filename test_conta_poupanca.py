from ContaPoupanca import ContaPoupanca
import pytest

@pytest.fixture
def conta_com_saldo_positivo():
    return ContaPoupanca(id_conta="23456", saldo=10000.00, taxa_de_rendimento_anual=0.10)

def test_depositar_valor_positivo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.depositar(valor_de_deposito=1000.00)
    assert conta_com_saldo_positivo.saldo == 11000.00

def test_depositar_valor_negativo(conta_com_saldo_positivo):
        with pytest.raises(ValueError, match="Valor de deposito inválido. Deve ser maior que zero."):
            conta_com_saldo_positivo.depositar(valor_de_deposito=-100.00)

def test_depositar_valor_usando_string(conta_com_saldo_positivo):
        with pytest.raises(TypeError, match="O valor do depósito deve ser do tipo float."):
            conta_com_saldo_positivo.depositar(valor_de_deposito="100.00")

def test_sacar_valor_positivo_menor_que_saldo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.sacar(valor_de_saque=1000.00)
    assert conta_com_saldo_positivo.saldo == 9000.00

def test_sacar_valor_positivo_maior_que_saldo(conta_com_saldo_positivo):
    with pytest.raises(ValueError, match="Saldo insuficiente para realizar o saque."):
            conta_com_saldo_positivo.sacar(valor_de_saque=40000.00)

def test_sacar_valor_negativo(conta_com_saldo_positivo):
        with pytest.raises(ValueError, match="Valor de saque inválido. Deve ser maior que zero."):
            conta_com_saldo_positivo.sacar(valor_de_saque=-100.00)

def test_sacar_valor_usando_string(conta_com_saldo_positivo):
        with pytest.raises(TypeError, match="O valor do saque deve ser do tipo float."):
            conta_com_saldo_positivo.sacar("100.00")

def test_get_saldo(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_saldo() == 10000.00

def test_get_id_conta(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_id_conta() == "23456"

def test_get_taxa_de_rendimento_anual(conta_com_saldo_positivo):
    assert conta_com_saldo_positivo.get_taxa_de_rendimento_anual() == 0.10

def test_set_saldo(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_saldo(novo_saldo=50.00)
    assert conta_com_saldo_positivo.saldo == 50.00

def test_set_id_conta(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_id_conta(novo_id="11111")
    assert conta_com_saldo_positivo.id_conta == "11111"

def test_set_taxa_de_rendimento_anual_usando_float(conta_com_saldo_positivo):
    conta_com_saldo_positivo.set_taxa_de_rendimento_anual(nova_taxa=0.20)
    assert conta_com_saldo_positivo.taxa_de_rendimento_anual == 0.20

def test_set_taxa_de_rendimento_anual_usando_valor_negativo(conta_com_saldo_positivo):
    with pytest.raises(ValueError, match="Taxa de rendimento inválida. Deve ser maior que zero."):
        conta_com_saldo_positivo.set_taxa_de_rendimento_anual(nova_taxa=-0.3)

def test_set_taxa_de_rendimento_anual_usando_usando_str(conta_com_saldo_positivo):
    with pytest.raises(TypeError, match="A nova taxa de rendimento deve ser do tipo float."):
        conta_com_saldo_positivo.set_taxa_de_rendimento_anual(nova_taxa="0.3")