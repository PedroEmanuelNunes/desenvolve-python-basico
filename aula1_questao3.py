# Entrada de dados
# leia n1, n2, n3
n1 = float(input("Digite o valor de n1: "))
n2 = float(input("Digite o valor de n2: "))
n3 = float(input("Digite o valor de n3: "))

m = (n1 + n2 + n3) / 3

# Processamento 
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# saída
print("Fim")