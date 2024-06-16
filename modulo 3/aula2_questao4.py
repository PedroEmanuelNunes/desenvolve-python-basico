# entrada de dados
# solicitando a classe (guerreiro, mago ou arqueiro)
# solicitando os pontos de força (de 1 a 20)
# solicitando os pontos de magia (de 1 a 20)
classe = input("Escolha a classe(guerreiro, mago ou arqueiro): ")
pontos_de_força = int(input("Digite os pontos de força(de 1 a 20): "))
pontos_de_magia = int(input("Digite os pontos de magia(de 1 a 20): "))

guerreiro = pontos_de_força >= 15 and pontos_de_magia <= 10
mago = pontos_de_força <= 10 and pontos_de_magia >= 15
arqueiro = 5 < pontos_de_força <= 15 and 5 < pontos_de_magia <= 15

valido = guerreiro or mago or arqueiro

print(f"Pontos de atributo consistentes com a classe escolhida: {valido}")
