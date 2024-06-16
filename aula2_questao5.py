# Entrada de dados 
# genero, idade e tempo de serviço
genero = input()
idade = int(input())
tempo = int(input())

# Processamento
# A: Para mulheres ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos.
# C: Ou ter 60 anos e trabalhando pelo menos 25.
a = (genero == "f" and idade >= 60) or (genero == "m" and idade >= 65)
b = tempo >= 30
c = idade >= 60 and tempo >= 25

pode_aposentar = a or b or c

# saida
print(pode_aposentar)