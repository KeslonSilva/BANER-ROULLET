#importa a biblioteca Random
import random
#pede para o usuario digitar os nomes
names_string = input("Qual a lista de pessoas que podem ser escolhidas ? ")
#junta os nomes em uma lista
names = names_string.split(", ")
#mede quantos itens tem na lista
num_itens = len(names)
#gera um numero aleatorio dentro da quantidade de itens da lista
random_choice = random.randint(0, num_itens -1)
#printa o nome correspondente a posição gerada aleatoriamente
print(" \n A pessoa quem vai pagar a conta hoje será o: " + names[random_choice])
print('\n')