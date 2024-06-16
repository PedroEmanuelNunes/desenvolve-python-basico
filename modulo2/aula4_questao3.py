# Leitura de dados
produto = (input(f"Digite o nome do produto 1: ")) # produto 1 = calça
preço_unitário_1 = float(input(f"Digite o preço unitário do produto 1: ")) # produto 1 = 199.90
quantidade_produto_1 = int(input(f"Digite a quantidade do produto 1: ")) # produto 1 = 3

produto = (input(f"Digite o nome do produto 2: ")) #  produto 2 = camisa
preço_unitário_2 = float(input(f"Digite o preço unitário do produto 2: ")) # produto 2 = 49.95
quantidade_produto_2 = int(input(f"Digite a quantidade do produto 2: ")) # produto 2 = 10

produto = (input(f"Digite o nome do produto 3 : ")) # produto 3 = cinto
preço_unitário_3 = float(input(f"Digite o preço unitário do produto 3: ")) # produto 3 = 25
quantidade_produto_3 = int(input(f"Digite a quantidade do produto 3 : ")) # produto 3 = 3

#Processamento
preço_1 = preço_unitário_1 * quantidade_produto_1
preço_2 = preço_unitário_2 * quantidade_produto_2
preço_3 = preço_unitário_3 * quantidade_produto_3

preço_total_produto = preço_1 + preço_2 + preço_3
total_compra = preço_total_produto

#Impressão de dados (saída)
print(f"Total: R${total_compra:,.2f}")





