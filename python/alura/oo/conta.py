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
    
    def saca(self, valor):
        self.__saldo -= valor
    
    # cohesion = The class has to have the only one responsability!!!
    # Encapsulamento
    def transfere(self, valor, destino):
        self.saca(valor) # self can call method as well. 
        destino.deposita(valor)
    
    # Getters
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    # Setters
    def set_limite(self, limite):
        self.__limite = limite
        