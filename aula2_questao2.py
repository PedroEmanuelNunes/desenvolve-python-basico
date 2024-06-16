# entrada de dados 
# idade de juliana
# idade de cris
idade_juliana = int(input())
idade_cris = int(input())

# processsamento
# true se pelo menos um dos dois for maior de idade 
# <exp1> juliana é maior de idade
# <exp2> cris é maior de idade
# <exp1> and <exp2>
# false em qualquer outro caso
pode_entrar = idade_juliana >= 18 or idade_cris >= 18

#saída 
print(pode_entrar)