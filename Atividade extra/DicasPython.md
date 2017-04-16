# Deixando código python mais elegante

Créditos a Raymonf Hettinger's, paletra de pycon 2013,  [video](http://www.youtube.com/watch?feature=player_embedded&v=OSGv2VnC0go)

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
