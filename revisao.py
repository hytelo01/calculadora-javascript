'''1 ) Entrada de dados
# comentando uma linha em python

Atribui-se uma variável e iguala ao comando de entrada de dados, chamada 'input'
'''
'''nome = input ("Qual o seu nome? ")'''

'''2) Saída de dados

É executda com o comando 'print', seguido da mensagem desejada 
'''
'''print (nome)'''

'''
3) Execução de um arqueivo na linguagem Python

É executado com o camando 'python', seguido do nome do arquivo e a extensão.

O comando é dado via terminal.

4) Concatenação da saída com as variaveis 

1ª - Usando virgulas
2ª - Usando chaves e o método '.format()', seguido da variável. 
3ª - Usando chaves e o método '.format()', seguido da variável, indicando a posição da variavel nas chaves.
4ª - Inicia-se com o comando 'f', seguida da mensagem entre aspas com as variáveis entre chaves e sem uso da vírgula

print ("Olá, ",nome)
print ("Olá, {} ".format(nome))
print ("Olá, {0} ".format(nome))

'''


'''a1 = input ("   Aluno 1: ") 
a2 = input ("   Aluno 2: ")
a3 = input ("   Aluno 3: ")
print ("Os alunos são: {0}, {1} e {2} ".format(a1, a2, a3))
print (f"Os alunos são: {a1}, {a2} e {a3} ")''''''

System.out.printl("Olá, mundo") Java 

5) Tipagem na entrada de dados

str - cadeia de caracteres 
int - números inteiros 
float - Números reais ou decimais
bool - valores logicos (Verdadeiro ou falso)'''

'''n1 = int(input ("Número 1: "))
n2 = int(input ("Número 2: "))
s = n1 + n2
print('A soma é ', s)'''

'''6) Programação sequencial

É a combinação dos comandos de entrada e saída de dados 

7) Programação condicional simples 

É composto pelos comandos if e else.
OBS: A estrutura é diferente das outras linguagens, não recebendo os parenteses e nem as chaves para cadas ação 

8) programação condicional composta
É compostos pelos comandos 
IF, ELIF e ELSE 

INCREMENTO - (+=)
DECREMENTO - (-=)

9) Programação de repetição com 'enquanto'
É usado o comando 'WHILE'
OBS: A estrutura é diferente das outras linguagens, não recebendo os parenteses e nem as chaves para cadas ação 

i = 10
while i >=1:
print (i)
i -= 1

i = 1
while i <=10:
print (i)
i += 1

10) Programação de repetição com 'Para'


É usado o comando 'for' e 'range'
for 'var' in range ('valor inicial', 'valor final', 'passo')
var - variavel
OBS: OS PARÂMENTROS NO COMANDO 'RANGE' NÃO SÃO TODOS OBRIGATÓRIOS

11) VETORES
É a coleção de dados de vários tipos representados por uma variável 

'''

'''n1 = int(input ("Número 1: "))
n2 = int(input ("Número 2: "))
m = ( n1 + n2 )/ 2

if n1 > n2:
    print (f"{n1} é maior que {n2}")
else:
    print (f"{n2} é maior que {n1}")

if m >= 7:
    print ("Média: ". m)
    print ("Aluno(a) aprovado(a): ")
elif m > 5 and m < 7:
    print ("Média: ". m)
    print ("Aluno(a) de recuperação: ")
else:
    print ("Média: ". m)
    print ("Aluno(a) reprovado: ")

for i in range (1,11): #INCREMENTO
    print(i)

for i in range (10,1, -1): #DECREMENTO
    print(i)'''

refri = ["Coca-cola", "Fanta", "Jesus", 123, 1.5, True, False]
print(refri[1])
print(type(refri[1]))

for r in refri:
    print(r)
    

