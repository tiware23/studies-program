#!/usr/bin/env python3

inteiros = [1,3,4,5,7,8,9]

# pares = []

# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(pares)

# List Comprehension

pares = [numero for numero in inteiros if numero % 2 == 0]
print(pares)

#arquivo copia.py
# logo = open('python-logo.png', 'rb')
# data = logo.read()
# logo.close()

# logo2 = open('python-logo2.png', 'wb')
# logo2.write(data)
# logo2.close()