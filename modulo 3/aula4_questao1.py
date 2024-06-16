# Entrada de dados 
n1,n2 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))
soma = n1 + n2

# Processamento 
if (soma % 2) == 0:
    resultado = "é par"
else:
    resultado = "é ímpar"

# saída
print(f"A soma dos números {n1} e {n2} é {soma}, que {resultado}.")