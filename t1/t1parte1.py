#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
# Questões do Trabalho 1 parte 1 da Disciplina de Paradigmas de Programação
# Aluno: Gabriel Doyle Balk
# 

# 1 Defina uma função somaQuad(x,y) que calcule a soma dos quadrados de dois números x e y.

def somaQuad(x,y): 
	return (x**2) + (y**2)

def main():
	print(somaQuad(2,3))

main()

# 2 Crie uma função hasEqHeads(l1,l2) que verifique se as listas l1 e l2 possuem o mesmo primeiro elemento.
# def hasEqHead(l1, l2)

def hasEqHead(l1, l2):
	return l1[0] in l2[0]

def main():
	print(hasEqHead(['gabriel', 'doyle', 'balk'], ['gabriel','cristovao','alfredo']))

main()

# 3 Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " 
#	adicionada ao início de cada nome. Defina uma função auxiliar para ajudar neste exercício.

def concatena_aux(l1):
	return 'Sr. ' + l1

def concatena(l1):
	return list(map(concatena_aux,l1))


def main():
	l1 = ['Gabriel','joão', 'Gustavo','josé','Manoel']
	print(concatena(l1))

main()


#4 Crie uma função que receba uma string e retorne o número de espaços nela contidos. 
# Defina uma função auxiliar para ajudar neste exercício.

def encontraEspacos_aux(char):
	return (char == " ")

def encontraEspacos(l1):
	return len(list(filter(encontraEspacos_aux, l1)))

def main():
	l1 = "estou muito feliz em estar aprendendo python"
	print(encontraEspacos(l1))
	
main()


#5 Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista. 
#Defina uma função auxiliar para ajudar neste exercício.

def resolve_aux(n):
	return 3*n*2 + 2/n + 1

def resolve(lista):
	return list(map(resolve_aux,lista))

def main():
	lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print(resolve(lista))

main()


#6 Escreva uma função que, dada uma lista de números, retorne uma lista com apenas os que forem negativos. 
#Defina uma função auxiliar para ajudar neste exercício.

def menorQueZero_aux(n):
	return n < 0

def menorQueZero(lista):
	return list(filter(menorQueZero_aux,lista))

def main():
	lista = [-1, -2, -3, 4, 5, 9, -4, -8, -12, 12, 18, 16, 0, -28]
	print(menorQueZero(lista))

main()

#7 Escreva uma função que receba uma lista de números e retorne somente os que estiverem entre 1 e 100,
# inclusive. Defina uma função auxiliar para ajudar neste exercício.
def entreUmeCem_aux(n):
	return (n >= 1  and n <= 100)

def entreUmeCem(lista):
	return list(filter(entreUmeCem_aux,lista))

def main():
	lista = [1,2,100,101,200,129,10,12,25,28,300,-100,-1,0]
	print(entreUmeCem(lista))

main()

#8 Escreva uma função que receba uma lista de números e retorne somente aqueles que forem pares.
#Defina uma função auxiliar para ajudar neste exercício.
def ehPar_aux(n):
	return (n % 2 == 0)

def ehPar(lista):
	return list(filter(ehPar_aux,lista))

def main():
	lista = [1,2, 3, 4, 5, 6, 7, 8, 9, 10,26]
	print(ehPar(lista))

main()

# 9 Crie uma função charFound(c,s) que verifique se o caracter c está contido na string. O resultado deve ser True ou False. 
#Você não deve usar o operador in. Defina uma função auxiliar para ajudar neste exercício.

def charFound(c,s):
	
	def aux(str):
		return c == str

	return bool(list(filter(aux, s)))

def main():
	string = 'isso é uma string'
	char = 'n'
	print (charFound(char,string))

main()	

#10 Escreva uma função que receba uma lista de strings e retorne uma nova lista com adição de marcações 
#HTML (p.ex.: <B> e </B>) antes e depois de cada string.

def addMarcacao_aux(s):
	return ('<B> '  + s + ' </B>')
	#deixei com um espaço antes e depois, não como é em HTML :/

def addMarcacao(lista):
	return list(map(addMarcacao_aux, lista))

def main():
	lista = ['hey hey', 'ho ho', 'haha']
	print(addMarcacao(lista))
main()

