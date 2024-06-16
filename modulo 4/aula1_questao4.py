# Entrada de dados
# Leia o valor de n
n = int(input("Digite o número de valores: "))

# Iniciliazar a variavel
maior = 0

# Processamento
while n > 0:
    x = int(input("Digite um valor: "))

    if x > maior:
        maior = x

    n -= 1

# saída
print("O maior valor é:", maior)
