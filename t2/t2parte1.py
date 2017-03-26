# Entregue os exercícios desta parte num arquivo chamado t2parte1.py. Os exercícios devem ser entregues em ordem e o enunciado
# de cada questão deve constar como comentário antes do código de cada resposta.

# 1 Defina uma função addSuffix(suf,nomes) que retorne a lista de nomes com o sufixo suf adicionado. Exemplos:
# addSuffix('@inf.ufsm.br',['fulano','beltrano']) 
# ['fulano@inf.ufsm.br', 'beltrano@inf.ufsm.br']
def addSuffix(suf, nomes):
	return  [nome + suf for nome in nomes]

def main():
	lista = ["Gabriel","Alfredo","gbalk"]
	suffix = "@inf.ufsm.br"
	l2 = addSuffix(suffix,lista)
	print(l2)

main()

# 2 Escreva uma função countShorts(words), que receba uma lista
# de palavras e retorne a quantidade de palavras dessa lista que possuem menos de 5 caracteres.
# t2.countShorts(['lazy','dog','brown','fox'])
#3

def countShorts(words):
	return len([word for word in words if len(word) < 5])

def main():
	lista = ['lazy','dog','brown','fox']
	lista2 = (countShorts(lista))
	print (lista2)

main()

# 3 Defina uma função stripVowels(s) que receba uma string e retire suas vogais,
# conforme os exemplos abaixo:
#>>> stripVowels('Andrea')
#'ndr'
#>>> stripVowels('xyz')
#'xyz'
#>>> stripVowels('')
#''


def stripVowels(string):
	blackList = "AEIOUaeiou"
	return "".join([ch for ch in string if ch not in blackList])

def main():
	frase = "Gabriel Doyle Balk"
	novaFrase = (stripVowels(frase))
	print(novaFrase)
main()

# 4 Defina uma função hideChars(s) que receba uma string, possivelmente contendo espaços, e que retorne outra string substituindo 
#os demais caracteres por '-', mas mantendo os espaços. Exemplos:
#>>> hideChars("Rio Grande do Sul")
#'--- ------ -- ---'
#>>> hideChars("")
#''

def isPace(char):
	return ' ' if char == ' ' else '-'

def hideChars(string):
	return "".join([isPace(char) for char in string])


def main():
	frase = "Rio Grande do Sul"
	novaFrase = hideChars(frase)
	print(novaFrase)

main()



# 5 Defina uma função que receba um número n e retorne uma tabela de números de 1 a n e seus quadrados, conforme os exemplos abaixo (você vai usar tuplas em Python):
#>>> genTable(5)
#[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
#>>> genTable(0)
#[]
#>>> genTable(1)
#[(1, 1)]

def genTable(n):
	return  [(num,num**2) for num in (range(1,n+1))]

def main():
	print(genTable(6))

main()


# 6 Defina uma função que receba uma lista de palavras e retorne uma string contendo o primeiro e o último caracter de cada palavra da lista. 
#Exemplo:
#>>> genCode(['abacaxi','mamao','banana'])
#'aimoba'

def conc(lista):
	return ()

def genCode(lista):
	return  "".join([(nome[0]+nome[-1]) for nome in lista])

def main():
	frutas = ['banana','melancia','pera','morango','laranja']
	print (genCode(frutas))

main()


# 7 Defina uma função myZip(l1,l2) que reproduza o comportamento da função zip do Python:
#>>> myZip([1,2,3],[4,5,6])
#[(1, 4), (2, 5), (3, 6)]
#>>> myZip([1,2,3],[4,5])
#[(1, 4), (2, 5)]

def myZip(l1,l2):
	return [(l1[i],l2[i]) for i in range(min(len(l1),len(l2)))]

def main():
	l1 = [1,2,3,8]
	l2 = [4,5,6]
	print(myZip(l1,l2))

main()



# 8 Escreva uma função enumerate(words) que numere cada palavra da lista recebida:
#>>> enumerate(['abacaxi','mamao','banana'])
#[(1, 'abacaxi'), (2, 'mamao'), (3, 'banana')]

def enumerate(lista):
	return [(i+1, lista[i]) for i in range(len(lista))]

def main():
	lista = ['abacaxi','banana','morango']
	print(enumerate(lista))

main()


# 9 Escreva uma função isBin(s) que verifique se a string recebida representa um número binário. Exemplo:
#>>> isBin('1010')

def isOneOrZero(num):
	return [n for n in num if n == '0' or n == '1']

def isBin(number):
	return len(number) == len(isOneOrZero(number))

def main():
	number = '01010010120'
	print(isBin(number))
main()



# 10 Escreva uma função bin2dec(digits), que receba uma lista de dígitos representando um número binário 
#e retorne seu equivalente em decimal. Exemplo:
#>>> bin2dec([1,1,1,1])
#15


def inverte(numbers):
	return numbers[::-1]

def toString(num):
	return "".join(str(n) for n in num)

def bin2dec(numbers):
	return sum([2**num for num in range(len(toString(numbers))) if inverte(toString(numbers))[num] == '1'])



def main():
	numBin = [1,1,1,1]
	print(bin2dec(numBin))	

main()