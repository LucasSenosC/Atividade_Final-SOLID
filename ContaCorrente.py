from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta: str, saldo: float, limite_da_conta: float):
        super().__init__(id_conta, saldo)

        if not isinstance(limite_da_conta, float):
            raise TypeError("O limite da conta deve ser do tipo float.")
        
        self.limite_da_conta: float = limite_da_conta

    def get_limite_da_conta(self):
        return self.limite_da_conta
    
    # O novo limite deve ser do tipo float e maior que zero.
    def set_limite_da_conta(self, novo_limite):
        if not isinstance(novo_limite, float):
            raise TypeError("O novo limite deve ser do tipo float.")
        if novo_limite < 0:
            raise ValueError("O novo limite deve ser não negativo.")
        self.limite_da_conta = novo_limite
    
    # Os valores de depósito dever ser do tipo float e maiores que zero.
    def depositar(self, valor_de_deposito):
        if not isinstance(valor_de_deposito, float):
            raise TypeError("O valor do depósito deve ser do tipo float.")
        if valor_de_deposito <= 0:
            raise ValueError("Valor de deposito inválido. Deve ser maior que zero.")
        self.set_saldo(self.get_saldo() + valor_de_deposito)
        print(f"Depósito no valor de R${valor_de_deposito:.2f} realizado com sucesso.")
        print(f"Saldo atual: R${self.get_saldo():.2f}")

    # Os valores de saque devem ser do tipo float, maiores que zero e menores ou iguais ao saldo mais o limite da conta.
    def sacar(self, valor_de_saque):
        if not isinstance(valor_de_saque, float):
            raise TypeError("O valor do saque deve ser do tipo float.")
        if valor_de_saque <= 0:
            raise ValueError("Valor de saque inválido. Deve ser maior que zero.")
        if self.get_saldo() + self.get_limite_da_conta() < valor_de_saque:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.set_saldo(self.get_saldo() - valor_de_saque)
        print(f"Depósito no valor de R${valor_de_saque:.2f} realizado com sucesso.")
        print(f"Saldo atual: R${self.get_saldo():.2f}")

