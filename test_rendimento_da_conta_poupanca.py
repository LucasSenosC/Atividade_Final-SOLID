from Rendimento_Da_Conta_Poupanca import Rendimento_Da_Conta_Poupanca
from ContaPoupanca import ContaPoupanca
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def rendimento():
    return Rendimento_Da_Conta_Poupanca()

@pytest.fixture
def conta_com_saldo_positivo():
    return ContaPoupanca(id_conta="23456", saldo=10000.00, taxa_de_rendimento_anual=0.05)

def test_verificar_rendimento_ao_ano_por_data_para_data_futura(conta_com_saldo_positivo, rendimento):
    data_futura = (datetime.today() + timedelta(days=365)).strftime("%d/%m/%Y %H:%M:%S")
    saldo_final = rendimento.verificar_rendimento_ao_ano_por_data(conta_poupanca = conta_com_saldo_positivo, data_informada=data_futura)
    assert saldo_final == pytest.approx(10498.25, abs=1e-2)

def test_verificar_rendimento_ao_ano_por_data_para_data_passada(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Data Inválida. Certifique-se de que seja uma data futura."):
        rendimento.verificar_rendimento_ao_ano_por_data(conta_poupanca = conta_com_saldo_positivo, data_informada="20/03/2023 00:00:00")

def test_verificar_rendimento_ao_ano_por_data_para_data_com_formato_errado(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="time data '37/03/2023 00:00:00' does not match format '%d/%m/%Y %H:%M:%S'"):
        rendimento.verificar_rendimento_ao_ano_por_data(conta_poupanca = conta_com_saldo_positivo, data_informada="37/03/2023 00:00:00")

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_com_saldo_positivo, rendimento):
    saldo_final=  rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=2, quantos_dias=2,
                                    quantas_horas=2, quantos_minutos=2, quantos_segundos=2)
    assert saldo_final == pytest.approx(11118.12, abs=1e-2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantos_anos_negativo(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de anos inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=-2, quantos_meses=2, quantos_dias=2,
                                    quantas_horas=2, quantos_minutos=2, quantos_segundos=2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantos_meses_negativo(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de meses inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=-2, quantos_dias=2,
                                    quantas_horas=2, quantos_minutos=2, quantos_segundos=2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantos_dias_negativos(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de dias inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=2, quantos_dias=-2,
                                    quantas_horas=2, quantos_minutos=2, quantos_segundos=2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantas_horas_negativas(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de horas inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=2, quantos_dias=2,
                                    quantas_horas=-2, quantos_minutos=2, quantos_segundos=2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantos_minutos_negativos(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de minutos inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=2, quantos_dias=2,
                                    quantas_horas=2, quantos_minutos=-2, quantos_segundos=2)

def test_verificar_rendimento_ao_ano_por_unidades_de_tempo_quantos_segundos_negativos(conta_com_saldo_positivo, rendimento):
    with pytest.raises(ValueError, match="Quantidade de segundos inválida. As quantidades de tempo devem ser não negativas"):
        rendimento.verificar_rendimento_ao_ano_por_unidades_de_tempo(conta_poupanca = conta_com_saldo_positivo, quantos_anos=2, quantos_meses=2, quantos_dias=2,
                                    quantas_horas=2, quantos_minutos=2, quantos_segundos=-2)