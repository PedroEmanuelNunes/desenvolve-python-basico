# entrada de dados 
# Solicitando a idade do usuário
idade = int(input("Digite sua idade: "))
partidas_jogadas = int(input("Digite quantas partidas você já jogou: "))
vitorias = int(input("Quantos jogos já venceu? "))

# processsamento
a = 16 <= idade <= 18
b = partidas_jogadas >= 3
c = vitorias >= 1

apto_para_ingressar = a and b and c 

# saída
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_para_ingressar}")

