class Conta:
    def __init__(self, id_conta: str, saldo: float = 0.0):

        if not isinstance(id_conta, str):
            raise TypeError("O id_conta deve ser do tipo string.")
        if not isinstance(saldo, float):
            raise TypeError("O saldo deve ser do tipo float.")
        
        self.id_conta: str = id_conta
        self.saldo: int = saldo
    
    def depositar(self, valor_de_deposito):
        pass

    def sacar(self, valor_do_saque):
        pass

    def get_id_conta(self):
        return self.id_conta

    def get_saldo(self):
        return self.saldo

    def set_id_conta(self, novo_id): 
        if not isinstance(novo_id, str):
            raise TypeError("O novo id deve ser do tipo string.")
        self.id_conta = novo_id

    def set_saldo(self, novo_saldo):
        if not isinstance(novo_saldo, float):
            raise TypeError("O novo saldo deve ser do tipo float.")
        self.saldo = novo_saldo