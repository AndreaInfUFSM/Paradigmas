
1 Considere a seguinte base de fatos e regras:

pai(roberto,joao).
pai(joao, jose).
pai(roberto,julio).
pai(julio,marcos).
pai(julio,mario).
avo(X,Z) :- pai(X,Y), pai(Y,Z).

Mostre o trace comentado das consultas:

?- avo(joao,Y).
false.
?- avo(roberto,Y).
Y = jose ;
Y = marcos ;
Y = mario.

   [trace] ?- avo(joao, Y).             Chama a função avo
   Call: (8) avo(joao, _4852) ? creep   Chama avô procurando um neto para João 
   Call: (9) pai(joao, _5070) ? creep   Procura se João é pai de alguem 
   Exit: (9) pai(joao, jose) ? creep    Encontra José como filho para João 
   Call: (9) pai(jose, _4852) ? creep   Procura um filho para José 
   Fail: (9) pai(jose, _4852) ? creep   Fail pois José não tem filho 
   Fail: (8) avo(joao, _4852) ? creep   Fail pois o filho de João não possui filho false.

2 Considere o predicado definido abaixo, que resolve um problema de uma prova da Olimpíada Brasileira de Informática.

azulejos(0,0).
azulejos(Na,Nq) :-
   Na > 0,
   Q is floor(sqrt(Na)),
   R is Na - Q*Q,
   azulejos(R,C),
   Nq is 1 + C.

Mostre o trace comentado desta consulta:

?- azulejos(120,A).

prolog [trace] ?- azulejos(120,A). 		- Chama a função azulejo enviando o valor 120 e a variável A. 
Call: (8) azulejos(120, _584) ? creep 	- Substitui A como uma variavel unica _584
 Call: (9) 120>0 ? creep - Regra, (n>0) é chamada 
 Exit: (9) 120>0 ? creep - Retorna regra true (120>0) 
 Call: (9) _812 is floor(sqrt(120)) ? creep - _812 recebe o retorno do calculo (floor(sqrt(120))) - igual ou menor numero inteiro da raiz de 120 
 Exit: (9) 10 is floor(sqrt(120)) ? creep - _812 recebeu 10 
 Call: (9) _824 is 120-10*10 ? creep - _824 recebe o retorno do calculo, sobra de azulejos
 Exit: (9) 20 is 120-10*10 ? creep - _824 recebeu 20 
 Call: (9) azulejos(20, _826) ? creep - Chamada recursiva da função azulejos enviando a variavel _824 e uma variavel auxiliar _826 
 Call: (10) 20>0 ? creep - Regra, (n>0) é chamada 
 Exit: (10) 20>0 ? creep - Retorno regra true (20>0) 
 Call: (10) _832 is floor(sqrt(20)) ? creep - _832 recebe o retorno do calculo (floor(sqrt(20))) - igual ou menor numero inteiro da raiz de 20 
 Exit: (10) 4 is floor(sqrt(20)) ? creep - _832 recebeu 4 
 Call: (10) _844 is 20-4*4 ? creep - _844 recebe o retorno do calculo, sobra de azulejos 
 Exit: (10) 4 is 20-4*4 ? creep - _844 recebeu 4 
 Call: (10) azulejos(4, _846) ? creep - Chamada recursiva da função azulejos enviando a variavel _844 e uma variavel auxiliar _846 
 Call: (11) 4>0 ? creep - Regra, (n>0) é chamada 
 Exit: (11) 4>0 ? creep - Retorno regra true (4>0) 
 Call: (11) _852 is floor(sqrt(4)) ? creep - _852 recebe o retorno do calculo (floor(sqrt(4))) - igual ou menor numero inteiro da raiz de 4 
 Exit: (11) 2 is floor(sqrt(4)) ? creep - _852 recebeu 2 
 Call: (11) _864 is 4-2*2 ? creep - _864 recebe o retorno do calculo, sobra de azulejos 
 Exit: (11) 0 is 4-2*2 ? creep - _864 recebeu 0 
 Call: (11) azulejos(0, _866) ? creep - Chamada recursiva da função azulejos enviando a variavel _864 e uma variavel auxiliar _866 
 Exit: (11) azulejos(0, 0) ? creep - Chamada recursiva da função azulejos enviando a 0 e 0 (n>0) false, retorna as funções 
 Call: (11) _870 is 1+0 ? creep - _870 recebe 0+1 
 Exit: (11) 1 is 1+0 ? creep - _870 recebeu o valor 1 
 Exit: (10) azulejos(4, 1) ? creep - Cria função azulejos(4, 1) 
 Call: (10) _876 is 1+1 ? creep - _876 recebe 1+1 
 Exit: (10) 2 is 1+1 ? creep - _876 recebe 2 
 Exit: (9) azulejos(20, 2) ? creep - Cria função azulejos(20, 2) 
 Call: (9) _584 is 1+2 ? creep - _584 recebe 1+2 
 Exit: (9) 3 is 1+2 ? creep - _584 recebe 3 
 Exit: (8) azulejos(120, 3) ? creep - Cria função azulejos(120, 3) A = 3 . - A recebe 3 

 


3 Escolha algum predicado recursivo que esteja nos slides ou em qualquer outra fonte. Faça a execução passo-a-passo de uma consulta com o predicado escolhido. Lembre-se de mostrar o código do predicado no seu arquivo t3parte1.md

 fatorial(3, X).					        Chama fatorial de 3
   Call: (7) fatorial(3, _G284) ? creep*	substitui X como uma variavel unica
   Call: (8) 3>0 ? creep					regra 2 meta 1(n>0) é invocada
   Exit: (8) 3>0 ? creep					objetivo tem sucesso
   Call: (8) _L205 is 3-1 ? creep			regra 2, meta 2 é chamada pra calcular 3-1
   Exit: (8) 2 is 3-1 ? creep				e sucesso
   Call: (8) fatorial(2, _L206) ? creep		Regra 2, objetivo 3 é invocada, chamada de nivel 2 fatorial(2, …)
   Call: (9) 2>0 ? creep					meta 1 (n>0) novamente para chamada fatorial
   Exit: (9) 2>0 ? creep					sucesso > 0
   Call: (9) _L224 is 2-1 ? creep			regra 2, chamada pra calcular 2-1
   Exit: (9) 1 is 2-1 ? creep				e sucesso
   Call: (9) fatorial(1, _L225) ? creep		regra2 é invocada: cahamda de nivel 3 para fatorial(1, …)
   Call: (10) 1>0 ? creep					meta 1 (n>0) de novo
   Exit: (10) 1>0 ? creep					e sucesso
   Call: (10) _L243 is 1-1 ? creep			chamada para calcular 1-1
   Exit: (10) 0 is 1-1 ? creep				e sucesso
   Call: (10) fatorial(0, _L244) ? creep	regra 2 é invocada:chamada recursiva para fatorial(0, …)
   Exit: (10) fatorial(0, 1) ? creep		dessa vez, regra 1 sucesso.
   Call: (10) _L225 is 1*1 ? creep			meta 
   Exit: (10) 1 is 1*1 ? creep				calculo ok, sem problemas
   Exit: (9) fatorial(1, 1) ? creep			nivel 3 do fat ok
   Call: (9) _L206 is 1*2 ? creep			meta
   Exit: (9) 2 is 1*2 ? creep				calculo ok, sem problemas
   Exit: (8) fatorial(2, 2) ? creep			chama nivel 2 do fatorial
   Call: (8) _G284 is 2*3 ? creep			meta
   Exit: (8) 6 is 2*3 ? creep				calculo ok, sem problemas
   Exit: (7) fatorial(3, 6) ? creep			entao chama o fat e retorno 6
