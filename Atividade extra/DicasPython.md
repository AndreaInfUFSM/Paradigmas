# Deixando código python mais elegante

Créditos a Raymonf Hettinger's, palestra de pycon 2013,  [video](http://www.youtube.com/watch?feature=player_embedded&v=OSGv2VnC0go)

Os exemplos de código e as citações diretas são todas da conversa de Raymond.
Eu estou traduzindo aqui para estudar e na esperança de que outros achem tão útil como eu achei

## Loop em um intervalo de números

```python
for i in [0, 1, 2, 3, 4, 5]:
    print i**2

for i in range(6):
    print i**2
```
### Melhor

```python
for i in xrange(6):
    print i**2
```

`Xrange` cria um iterador sobre o intervalo produzindo os valores um de cada vez.É muito mais eficiente em termos de memória do que `range`. `Xrange` foi renomeado para`range` em python 3.

## Loop em uma collection
```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print colors[i]
```

### Melhor

```python
for color in colors:
    print color
```
## Looping para trás

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print colors[i]
```

### Melhor

```python
for color in reversed(colors):
    print color
    
## Loop em uma collection e indices

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print i, '--->', colors[i]
```

### Melhor

```python
for i, color in enumerate(colors):
    print i, '--->', color
```
É rápido e bonito e nos evita de seguir os índices individuais e de os incrementar.
Sempre que você estiver manipulando índices [em uma coleção], você provavelmente está fazendo errado.
 
