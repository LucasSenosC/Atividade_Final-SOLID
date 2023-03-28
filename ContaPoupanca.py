from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta: str, saldo: float, taxa_de_rendimento_anual: float):
        super().__init__(id_conta, saldo)

        if not isinstance(taxa_de_rendimento_anual, float):
            raise TypeError("O taxa de rendimento anual da conta deve ser do tipo float.")
        self.taxa_de_rendimento_anual: float = taxa_de_rendimento_anual

    def get_taxa_de_rendimento_anual(self):
        return self.taxa_de_rendimento_anual
    
    # A nova taxa deve ser do tipo float e maior que zero.
    def set_taxa_de_rendimento_anual(self, nova_taxa):
        if not isinstance(nova_taxa, float):
            raise TypeError("A nova taxa de rendimento deve ser do tipo float.")
        if nova_taxa <= 0:
            raise ValueError("Taxa de rendimento inválida. Deve ser maior que zero.")
        self.taxa_de_rendimento_anual = nova_taxa

    # Os valores de depósito dever ser do tipo float e maiores que zero.
    def depositar(self, valor_de_deposito):
        if not isinstance(valor_de_deposito, float):
            raise TypeError("O valor do depósito deve ser do tipo float.")
        if valor_de_deposito <= 0:
            raise ValueError("Valor de deposito inválido. Deve ser maior que zero.")
        self.set_saldo(self.get_saldo() + valor_de_deposito)
        print(f"Depósito no valor de R${valor_de_deposito:.2f} realizado com sucesso.")
        print(f"Saldo atual: R${self.get_saldo():.2f}")

    # Os valores de saque devem ser do tipo float, maiores que zero e menores ou iguais ao valor do saldo da conta.
    def sacar(self, valor_de_saque):
        if not isinstance(valor_de_saque, float):
            raise TypeError("O valor do saque deve ser do tipo float.")
        if valor_de_saque <= 0:
            raise ValueError("Valor de saque inválido. Deve ser maior que zero.")
        if self.get_saldo() < valor_de_saque:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.set_saldo(self.get_saldo() - valor_de_saque)
        print(f"Depósito no valor de R${valor_de_saque:.2f} realizado com sucesso.")
        print(f"Saldo atual: R${self.get_saldo():.2f}")


