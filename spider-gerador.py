import random
##By: spiderckz
##Gay: nerox
print('| CC GENERATOR |')
print('| BY SPIDERCKZ |')
print('vers茫o 1.0')
print ('instagram: spidercks')
print('--------------------------------------------------------')
y = True
Y = True
N = False
n = False
list = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
nume = random.randrange(1, 9999999999999999)
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99799989999)

bi = str(input('Gerar v谩rias ccs? y/n?: '))

if bi == 'y':
    nume2 = random.randrange(1, 9999999999)
    bin = int(input('Bin de 6 n煤meros: '))
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    print('para usar o script novamente digite "python3 spider-gerador.py"')
    
else:
    nume2 = random.randrange(1, 9999999999)
    bin = int(input('Bin de 6 n煤meros: '))
    print('馃挸CC:', bin, nume2)
    print('馃攼Cvv:', cvv)
    print('馃搯Vencimento:', data1, data2, data3)
    print('馃搩CPF:', cpf)
    print('--------------------------------------------------------')
    print('para usar o script novamente digite "python3 spider-gerador.py"')
    
