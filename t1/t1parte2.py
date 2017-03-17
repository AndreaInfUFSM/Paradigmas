#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Questões do Trabalho 1 parte 2 da Disciplina de Paradigmas de Programação
# Aluno: Gabriel Doyle Balk
# 

#Parte 2

#1 Entregue esta parte num arquivo chamado t2parte1.py. Estes exercícios também devem ser entregues em ordem e 
#com o enunciado em forma de comentário. Nesta Parte 2, todos os exercícios devem usar funções anônimas (lambda).
#Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " adicionada ao início de cada nome.

def main():
	lista = ['Gabriel','joão', 'Gustavo','josé','Manoel']
	print (list(map(lambda nomes: 'Sr. '+ nomes, lista)))
	
main()

#2 Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista.
def main():
	lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print (list(map(lambda n: 3*n*2 + 2/n + 1, lista)))

main()

#3 Crie uma função que receba uma lista de nomes e retorne outra lista com somente aqueles nomes que terminarem com a letra 'a'.
def main():
	lista = ['Gabriel','joão', 'Gustavo','josé','Manoel', 'joana']
	print (list(filter(lambda s: s[-1] == 'a', lista)))

main()

#4 Escreva uma função que, dada uma lista de idades de pessoas no ano atual, retorne uma lista somente com as idades 
# de quem nasceu depois de 1970. Para testar a condição, sua função deverá subtrair a idade do ano atual. Exemplo de uso:
#>>> idades([20,30,51,57])
#[20, 30]

def main():
	lista = [20, 30, 51, 57, 47, 46]
	print (list(filter(lambda id: 2017 - id > 1970, lista )))


main()


#5 código abaixo é escrito em Python imperativo. Escreva um código equivalente usando programação funcional.

#numbers = [1, 2, 3, 4]
#new_numbers = []
#for number in numbers:
# new_numbers.append(number * 2)
#print(new_numbers)
def main():
	numbers = [1, 2, 3, 4]
	new_numbers = list(map(lambda n: n* 2, numbers))
	print(new_numbers)
	#acho que como cria um novo vetor ficaria assim, mas também daria pra printar direto né?

main()

