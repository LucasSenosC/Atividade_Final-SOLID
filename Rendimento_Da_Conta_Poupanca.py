from ContaPoupanca import ContaPoupanca
from datetime import datetime

class Rendimento_Da_Conta_Poupanca:

    # Este método recebe uma ContaPoupanca e uma data futura.
    # O método calcula o rendimento do saldo presente dentro da conta até a determinada data que foi passada como argumento.
    # A data deve vir no formato %d/%m/%Y %H:%M:%S (string)
    def verificar_rendimento_ao_ano_por_data(self, conta_poupanca: ContaPoupanca, data_informada: str):
        if not isinstance(data_informada, str):
            raise TypeError("A data de verificação deve ser do tipo string.")
        data_atual = datetime.today()
        data_de_verificacao = datetime.strptime(data_informada, "%d/%m/%Y %H:%M:%S")
        fracao_dos_anos_decorridos = (data_de_verificacao - data_atual).days / 365.25
        if fracao_dos_anos_decorridos < 0:
            raise ValueError("Data Inválida. Certifique-se de que seja uma data futura.")
        saldo_pos_rendimento = conta_poupanca.get_saldo() * (1 + conta_poupanca.get_taxa_de_rendimento_anual())**fracao_dos_anos_decorridos
        conta_poupanca.set_saldo(saldo_pos_rendimento)
        print(f"Saldo atual: R${conta_poupanca.get_saldo():.2f}")
        return saldo_pos_rendimento
        
    # Este método recebe uma ContaPoupanca e uma relação de anos, meses, dias, horas, minutos e segundos.
    # O método calcula o rendimento do saldo presente dentro da conta após ter passado o total de tempo informado.
    # As quantidades de anos, meses... até segundos devem devem ser inteiras e maiores que zero
    def verificar_rendimento_ao_ano_por_unidades_de_tempo(self, conta_poupanca: ContaPoupanca, quantos_anos: int, quantos_meses: int, quantos_dias: int,
                                    quantas_horas: int, quantos_minutos: int, quantos_segundos: int):
        if quantos_anos < 0:
            raise ValueError("Quantidade de anos inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos = quantos_anos
        if quantos_meses < 0:
            raise ValueError("Quantidade de meses inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos += quantos_meses/12
        if quantos_dias < 0:
            raise ValueError("Quantidade de dias inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos += quantos_dias/365
        if quantas_horas < 0:
            raise ValueError("Quantidade de horas inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos += quantas_horas/8760
        if quantos_minutos < 0:
            raise ValueError("Quantidade de minutos inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos += quantos_minutos/525600
        if quantos_segundos< 0:
            raise ValueError("Quantidade de segundos inválida. As quantidades de tempo devem ser não negativas")
        tempo_total_em_anos += quantos_segundos/31536000

        saldo_pos_rendimento = conta_poupanca.get_saldo() * (1 + conta_poupanca.get_taxa_de_rendimento_anual()) ** tempo_total_em_anos
        conta_poupanca.set_saldo(saldo_pos_rendimento)
        print(f"Saldo atual: R${conta_poupanca.get_saldo():.2f}")
        return saldo_pos_rendimento