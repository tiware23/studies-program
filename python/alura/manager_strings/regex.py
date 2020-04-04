import re
email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 91234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular 83133131"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email3)

# print(retorno)

frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"


defu = "[0-9]{2}h"
defu_n = "[a-z]{1,10}[ ][0-9]{1,2}[h]"

retorno_string = re.search(defu_n, frase3)



print(retorno_string.group())