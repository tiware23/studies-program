from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=2500"

argumentoUrl = ExtratorArgumentosUrl(url)
argumentoUrl2 = ExtratorArgumentosUrl(url2)

print(argumentoUrl == argumentoUrl2)
# moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
# valor = argumentoUrl.extraiValor()
# print(moedaOrigem, moedaDestino, valor)
# print(argumentoUrl)

# index = url.find("moedadestino") + len("moedadestino") + 1
# subString = url[index:]
# print(subString)
# print(index)

'''
#argumento = "https://www.butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar$valor=1500"
argumento = "https://www.butebank.com.br/cambio?moedaorigem=real"
#............012345678910

subString = argumento[5:11]

print(subString)
'''

# argumento = "moedaorigem=real"
#
# listaArguementos = argumento.split("=")
# print(listaArguementos)

# index = argumento.find("=")
# subString = argumento[index + 1:]
# print(subString)



# celular = "(41)96574-172"
#
# x = celular.find("(") + 1
# y = celular.find(")")
#
# print(x, y)
#
# indiceInicialCodigoArea = x
# indiceFinalCodigoArea = y
#
# print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])

# url_final = "www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar"
# url = "pagina?argumentos"
# index = url.find("?")
# print(url[index + 1:])


# string = "bytebankbyte"
# stringNova = string.replace("byte", "Thiago",1)
# print(stringNova)





