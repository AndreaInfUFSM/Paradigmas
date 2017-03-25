#Entregue esta parte num arquivo chamado t2parte2.py. Este arquivo deverá ter uma cópia de svgcolors.py, 
#com as alterações solicitadas abaixo:

#Reimplemente a função genRects para gerar uma lista com o número correto de retângulos, nas posições corretas, usando os argumentos n, w e h.
# A figura produzida deverá ser igual a colors.svg. Use list comprehension.

#Note que a lista styles, na função main(), contém strings que especificam as cores dos retângulos. 
#Essa lista é definida com strings fixas (não é gerada por uma função). Crie uma função para gerar essa lista de cores, 
#tendo no mínimo um parâmetro que defina a quantidade (n) de cores a serem geradas. Você pode usar qualquer esquema de geração de cores, 
#por exemplo produzindo n variações de vermelho, etc. Use sua criatividade :-)

#!/usr/bin/env python3
import itertools

'''
   Programacao funcional para gerar SVG:
   - gera uma lista de coordenadas de retangulos
   - define uma lista de estilos (cores), em qualquer quantidade
   - aplica os estilos aos retangulos, gerando uma lista com todos os dados para o SVG
   - coloca os dados no formato SVG, concatenando strings
'''

def svgRect(rs):
   (((x,y),w,h),style) = rs
   return "<rect x='%.3f' y='%.3f' width='%.2f' height='%.2f' style='%s'/>\n" % (x,y,w,h,style)

def svgImage(w, h, rs):
   return "<svg width='%.2f' height='%.2f' xmlns='http://www.w3.org/2000/svg'>\n" % (w,h) + \
          ''.join(map(svgRect, rs)) + "</svg>"

def applyStyles(rects, styles):
   return list(zip(rects, itertools.cycle(styles)))

# TODO: modifique essa funcao para gerar mais retangulos
def genRects(n, w, h):
   return [((n,0.0),w,h) for n in range(0,500,50)]


def writeFile(fname, contents):
   f = open(fname, 'w')
   f.write(contents)
   f.close()

def genFill():
	return ["fill:rgb(%s, %s, %s)" % (25,num,15) for num in range(1,140,14)]


def main():
   maxWidth = 1000
   maxHeight = 100
   rects = genRects(10,50,50)
   styles = genFill()
   rectstyles = applyStyles(rects, styles)
   writeFile("mycolors.svg", svgImage(maxWidth, maxHeight, rectstyles))
   

if __name__ == '__main__':
   main()
