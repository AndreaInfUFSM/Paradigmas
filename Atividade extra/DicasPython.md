# Deixando código python mais elegante

Créditos a Raymonf Hettinger's, palestra de pycon 2013,  [video](http://www.youtube.com/watch?feature=player_embedded&v=OSGv2VnC0go)

Os exemplos de código e as citações diretas são todas da conversa de Raymond.
Eu estou traduzindo aqui para estudar e na esperança de que outros achem tão útil como eu achei

## Loop em um intervalo de números

```python
for i in [0, 1, 2, 3, 4, 5]:
    print (i**2)
 ```
### Melhor
```python
for i in range(6):
    print (i**2)
```
nota: em python 2 use xrange

## Loop em uma collection

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print (colors[i])
```

### Melhor

```python
for color in colors:
    print (color)
```
## Loop para trás

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print (colors[i])
```

### Melhor

```python
for color in reversed(colors):
    print (color)
```  
## Loop em uma collection e indices

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print (i, '--->', colors[i])
```

### Melhor

```python
for i, color in enumerate(colors):
    print (i, '--->', color)
```
É rápido e bonito e nos evita de seguir os índices individuais e de os incrementar.
Sempre que você estiver manipulando índices [em uma coleção], você provavelmente está fazendo errado.
 
## Loop sobre duas collections

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print (names[i], '--->', colors[i])
```
### Melhor

```python
for name, color in zip(names, colors):
    print (name, '--->', color)
```

## Loop em ordem ordenada

```python
colors = ['red', 'green', 'blue', 'yellow']

# Ordem "frente para trás"
for color in sorted(colors):
    print (colors)

# Ordem "trás para frente"
for color in sorted(colors, reverse=True):
    print (colors)
```
## Ordem Personalizada

```python
colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print (sorted(colors, cmp=compare_length))
```

### Melhor

```python
print (sorted(colors, key=len))
```

O original é lento e desagradável para escrever. Além disso, as funções de comparação não estão mais disponíveis no python 3.


## Construindo um dictionary em pares

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
# {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
```
