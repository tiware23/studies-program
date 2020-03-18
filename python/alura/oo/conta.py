class Conta:
    def __init__(self,numero, titular, saldo, limite=1000.0):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar): # In a Class methods could be private. (__pode_sacar)
        total_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= total_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    
    # cohesion = The class has to have the only one responsability!!!
    # Encapsulamento
    def transfere(self, valor, destino):
        self.saca(valor) # self can call method as well. 
        destino.deposita(valor)
    
    # Getters
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    # Setters
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco(): # Static methods
        return {'BB': '001', 'Caixa': '104', 'Bradeso': '237'} 
