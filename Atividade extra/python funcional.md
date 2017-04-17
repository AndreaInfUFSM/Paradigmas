Créditos ao site [python help](https://pythonhelp.wordpress.com) de onde tirei o conteúdo para meu estudo e estou disponibilizando aqui para que outras pessoas possam usufruir tanto quanto eu.


Os exemplos de código e as citações diretas são todas da conversa de Raymond.
Eu estou traduzindo aqui para estudar e na esperança de que outros achem tão útil como eu achei

## MAP( ), REDUCE( ), FILTER( ) E LAMBDA

### Map( )

map( ) é uma função builtin de Python, isto é, uma função que é implementada diretamente no interpretador Python, podendo ser utilizada sem a importação de um módulo específico. Essa função, em Python, serve para aplicarmos uma função a cada elemento de uma lista, retornando uma nova lista contendo os elementos resultantes da aplicação da função. 
Considere o exemplo abaixo:


```python
lista1 = [1, 4, 9, 16, 25]
lista2 = map(math.sqrt, lista1)
print (lista2)
[1.0, 2.0, 3.0, 4.0, 5.0]
```
Ao chamar a função map(math.sqrt, lista1), estamos solicitando ao interpretador para que execute a função math.sqrt (raiz quadrada) usando como entrada cada um dos elementos de lista1, e inserindo o resultado na lista retornada como resultado da função map().

É uma forma bem interessante e expressiva de denotar a aplicação de uma função a cada elemento de uma lista (ou sequência). Mas, podemos facilmente substituir uma chamada a map() por list comprehensions. O código recém listado poderia ser substituído por:
```python
lista2 = [math.sqrt(x) for x in lista1]
print lista2
[1.0, 2.0, 3.0, 4.0, 5.0]
```
O código acima produz o mesmo resultado que map(), pois, para cada elemento de lista1, executa a função math.sqrt e inclui o resultado dessa execução na lista de retorno.

### reduce()
reduce() é outra função builtin do Python (deixou de ser builtin e passou a estar disponível no módulo functools a partir da versão 3000). 
Sua utilidade está na aplicação de uma função a todos os valores do conjunto, de forma a agregá-los todos em um único valor. Por exemplo, para aplicar a operação de soma a todos os elementos de uma sequência, de forma que o resultado final seja a soma de todos esses elementos, poderíamos fazer o seguinte:
```python
 import operator #necessário para obter a função de soma
 valores = [1, 2, 3, 4, 5]
 soma = reduce(operator.add, valores)
 print (soma)
 15
```
É claro que, para realizar a soma de todos os elementos de uma sequência, é muito mais claro utilizarmos a função sum():
```python
print sum(valores)
15
```
Como falei anteriormente, reduce() foi retirada do conjunto de builtins de Python.

### filter()
Como o próprio nome já deixa claro, filter() filtra os elementos de uma sequência. O processo de filtragem é definido a partir de uma função que o programador passa como primeiro argumento da função. Assim, filter() só “deixa passar” para a sequência resultante aqueles elementos para os quais a chamada da função que o usuário passou retornar True. Vejamos um exemplo:
```python
 def maior_que_zero(x):
     return x > 0

valores = [10, 4, -1, 3, 5, -9, -11]
print filter(maior_que_zero, valores)
[10, 4, 3, 5]
```
No exemplo acima, filter() chamou a função maior_que_zero para cada um dos elementos contidos em valores. Se a função retornar True, o elemento é inserido na lista de resultado. Caso contrário, não o é. Ou seja, é feita a filtragem e só passam aqueles elementos que são maiores que zero.

Assim, como no exemplo da builtin map(), aqui também podemos escrever com facilidade uma comprehension com a mesma funcionalidade:

```python
 print [x for x in valores if x > 0]
[10, 4, 3, 5]
```

### lambda
No exemplo da função filter(), tivemos que definir uma nova função (chamada maior_que_zero) para usar somente dentro da função filter(), sendo chamada uma vez para cada elemento. Ao invés de definir uma nova função dessa forma, poderíamos definir uma função válida somente enquanto durar a execução do filter. Não é necessário nem dar um nome a tal função, sendo portanto chamada de função anônima ou função lambda. Considere o exemplo abaixo:
```python
valores = [10, 4, -1, 3, 5, -9, -11]
print filter(lambda x: x > 0, valores)
[10, 4, 3, 5]
```
Definimos uma função anônima (portanto, não tem nome), que recebe uma entrada (a variável x) e retorna o resultado da operação x > 0, True ou False.

Poderíamos também usar uma função lambda no exemplo da função reduce():
```python
valores = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, valores)
 print soma
15
```
No código acima, definimos uma função anônima que recebe duas entradas e retorna a soma dessas entradas.

### Função Range() em Python

A função range() retorna uma série numérica no intervalo enviado como argumento.

### Estrutura da função
```python
 range(stop) # primeira definição ou definição simplificada
 range(start, stop, step) # segunda definição ou definição completa
 ```
A função range() exige a definição do último elemento da sequência numérica. 
Por padrão, o parâmetro start será igual a 0 e o step igual a 1.

* start - início da sequência
* stop - último elemento da sequência
* step - intervalo entre os elementos
```python
list(range(5))
# [0, 1, 2, 3, 4]
```
A função retornou uma lista contendo 5 elementos, onde o primeiro é o 0 e o último 4.
O primeiro elemento é igual a 0, até porque, quando não definido, assume-se que start=0. O último elemento é o 4, 
```python
list(range(2, 6))
# [2, 3, 4, 5]
```
No código acima, definimos o parâmetro start=2 e stop=6 logo, o primeiro elemento foi o 2, 
enquanto o último elemento, igual a 5.
```python
list(range(2, 10, 2))
# [2, 4, 6, 8]
```
No código acima, geramos a sequência no intervalo de 2 à 10 e com o step igual a 2.
Logo foram impressos 4 elementos no intervalo de 2 à 10.

```python
list(range(0, 30, 3))
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```
Definimos uma segunda sequência numérica no intervalo de 0 à 30 e o step igual a 3.

