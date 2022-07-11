#!/usr/bin/python3
#Vídeo 19 da playlist https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=19

'''
PRINT METHOD: print(objects, sep, end, file, flush)
objects (objetos): objetos a serem printados. "*" indica que há mais de um objeto
sep (separador): Especifica como os objetos serão separados, se houver mais do que um.
end (caractere): Especifica o caractere que é impresso no final da linha.
file (arquivo): Especifica um objeto com um método write, com um arquivo.
flush (liberar): Valor booleano que especifica se a saída é eliminada (True) ou gravada em buffer (False).
'''
#backslash (barra invertida) "\": "\t" = tabulação; "\n" = nova linha; \' = aspas simples; \" = aspas dupla;
#"\\" = barra invertida; "\r" = retorna o curso para 1ª linha, "\b" = retrocede apagando; "\f" = avanço de formulário;
#"\ooo" = valor octagonal; "\xhh" = valor hexadecimal; "\v" = espaço vertical; "\0" = valor binário

'''
SORT METHOD sort(objects, reverse = True|False, Key=myFunc)
reverse (opcional): se verdadeiro ordena descendente, se falso ordena crescente.
key (opcional): função definida pelo usuário ou do sistema, para especificar um critério de ordenação.
'''

li = [9,1,8,2,7,3,6,4,5] #Definição de uma lista de valores inteiros

s_li = sorted(li) #Definição de uma nova lista ordenada da lista li

print('\nSorted Variable:\t', s_li) #Imprime a lista s_li

li.sort() #Ordena a lista li sem retornar qualquer resultado, funciona somente para listas, não funciona para tuple (não muda)

print('\nSorted Variable:\t', li) #Imprime a lista li

s_liRev = sorted(li, reverse=True) #Definição de uma nova lista ordenada da lista li em ordem decrescente

print('\nSorted Variable:\t', s_li) #Imprime a lista s_liRev

li.sort(reverse=True) #Ordena a lista li na ordem decrescente sem retornar qualquer resultado

print('\nSorted Variable:\t', li) #Imprime a lista li

tup = (9,1,8,2,7,3,6,4,5) #Define uma tuple de valores

s_tup = sorted(tup) #Definição de uma nova lista de ordenada da tuple tup

print('\nTuple\t', s_tup) #Imprime a tuple s_tup

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'} #Define de um variável dictionary (estrutura de dados
									#armazenado na forma de pares de chave-valores

s_di = sorted(di) #Definição de uma nova lista ordenada das chaves do dicionário

print('\nDict\t', s_di) #Imprime a lista s_di

li = [-6, -5,-4,1,2,3] #Definição de uma lista de valores

print()
print(li,'\n')

s_li = sorted(li, key=abs) #Definição de uma nova lista ordenada onde os valores foram ordenados no seu valor absoluto
print(s_li,'\n') #Imprime a lista s_li

from operator import attrgetter 

'''
operator = Módulo de funções de operadores padrões do Python, é um módulo do python que exporta um conjunto de funções eficientes
correspondentes aos operadores intrínsecos do Python
attrgetter = retorna os atributo de um objetos
'''

class Employee(): #Define de uma classe Employee
    def __init__(self, name, age, salary): #Atribuição de valores à classe quando for criado a classe Employee
        self.name = name #Atribuição do valor name repassado à variável self.name
        self.age = age #Atribuição do valor age repassado à variável self.age
        self.salary = salary #Atribuição do valor salary repassado à variável self.name

    def __repr__(self): #Definição da representação em string de um objeto a ser retornado
        return '({},{},${})'.format(self.name, self.age, self.salary) #Retorna a representação do objeto passado para a classe Employee

e1 = Employee('Carl', 37, 70000) #Definição da variável e1 como uma classe Employee e retorna uma tuple
e2 = Employee('Sarah', 29, 80000) #Definição da variável e2 como uma classe Employee e retorna uma tuple
e3 = Employee('John', 43, 90000) #Definição da variável e3 como uma classe Employee e retorna uma tuple

employees = [e1,e2,e3] #Definição de uma nova lista employees como uma lista de classe Employee

'''
s_employees = sorted(employees)
Não há como ordenar uma lista de classes diretamente precisa criar uma função para definir o que quer que seja ordenado
'''

def e_sort(emp): #Definição de uma função para indicar o que será utilizado para ordenar
    return emp.name

s_employees = sorted(employees, key=e_sort) #Definição de uma nova lista ordenada de classes baseado na chave definida na função e_sort

print(s_employees) #Imprime a lista de classes s_employees

s_employees = sorted(employees, key=lambda e: e.salary) #Definição de uma nova lista ordenada de classes baseado na chave definida na função lambda

print(s_employees) #Imprime a lista de classes s_employees

s_employees = sorted(employees, key=attrgetter('age'), reverse=True) #Definição de uma nova lista ordenada de classes na ordem decrescente, baseado
								     #na chave obtida na função attrgetter que retorna os atributos da variável age
								     #da classe Employee'''

print(s_employees) #Imprime a lista de classes s_employees
