def cria_conta(numero, titular, saldo, limiete):
    conta = {"numero": numero, "titular": titular, "saldo": saldo}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo: é {}".format(conta["saldo"]))