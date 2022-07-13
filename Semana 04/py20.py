#!/usr/bin/python3

'''
Vídeo 20 da playlist https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=20

f = open('testfile.txt')
Traceback (most recent call last):
  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py20.py", line 4, in <module>
    f = open('testfile.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'
'''

try: #permite testar um bloco de códigos quanto aos erros
    f = open('testfile.txt') # caso ocorra um erro ao abrir o arquivo executa a exceção
except Exception: #trata os erros de forma geral
    print('Sorry. This file does not exist\n')

try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') # caso ocorra um erro ao abrir o arquivo executa a exceção
    var = bad_var #força um erro de variável não definida
except Exception: #trata os erros de forma geral
    print('Sorry. This file does not exist\n')

'''
try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') # caso ocorra um erro ao abrir o arquivo executa a exceção
    var = bad_var #força um erro de variável não definida
except FileNotFoundError: #trata os erros de forma geral
    print('Sorry. This file does not exist\n')

Traceback (most recent call last):
  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py20.py", line 26, in <module>
    var = bad_var #força um erro de variável não definida
NameError: name 'bad_var' is not defined
'''

try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') #caso ocorra um erro ao abrir o arquivo executa a exceção
    var = bad_var #força um erro de variável não definida
except FileNotFoundError: #trata o erro específico de arquivo não encontrado
    print('Sorry. This file does not exist\n')
except Exception: #trata os erros de forma geral
    print('Sorry. Something went wrong\n')

try: #permite testar um bloco de códigos quanto aos erros
    f = open('testfile.txt') #caso ocorra um erro ao abrir o arquivo executa a exceção
    var = bad_var #força um erro de variável não definida
except FileNotFoundError as e: #trata o erro específico de arquivo não encontrado
    print(str(e) + '\n')
except Exception as e: #trata os erros de forma geral
    print(str(e) + '\n')

try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') #caso ocorra um erro ao abrir o arquivo executa a exceção
    var = bad_var #força um erro de variável não definida
except FileNotFoundError as e: #trata o erro específico de arquivo não encontrado
    print(str(e) + '\n')
except Exception as e: #trata os erros de forma geral
    print(str(e) + '\n')

try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') # tenta abrir o arquvio e caso ocorra um erro executa a exceção específica ou genéria na sequência de exceções
except FileNotFoundError as e: # trata o erro e atribui o código de erro a uma variável
    print(str(e) + '\n')
except Exception as e: # trata os erros de forma geral e atribui o erro a uma varíavel
    print(str(e) + '\n')
else: # executa um código quando não há erro
    print(f.read())
    f.close()

try: #permite testar um bloco de códigos quanto aos erros
    f = open('test_file.txt') # tenta abrir o arquvio e caso ocorra um erro executa a exceção específica ou genéria na sequência de exceções
except FileNotFoundError as e: # trata o erro e atribui o código de erro a uma variável
    print(e)
except Exception as e: # trata os erros de forma geral e atribui o erro a uma varíavel
    print(e)
else: # executa um código quando não há erro
    print(f.readline(19))
    f.close()
finally: # Executa o código independentemente do resultado dos blocos try e except, porém executará também os blocos de exceção e else
    print("Executing Finally...\n")

try: #permite testar um bloco de códigos quanto aos erros
    f = open('testfile.txt') # tenta abrir o arquvio e caso ocorra um erro executa a exceção específica ou genéria na sequência de exceções
except FileNotFoundError as e: # trata o erro e atribui o código de erro a uma variável
    print(e)
except Exception as e: # trata os erros de forma geral e atribui o erro a uma varíavel
    print(e)
else: # executa um código quando não há erro
    print(f.read())
    f.close()
finally: # Executa o código independentemente do resultado dos blocos try e except, porém executará também os blocos de exceção e else
    print("Executing Finally...\n")

try: #permite testar um bloco de códigos quanto aos erros
    f = open('currupt_file.txt') # tenta abrir o arquvio e caso ocorra um erro executa a exceção específica ou genéria na sequência de exceções
    if f.name == 'currupt_file.txt': # força um erro manualmente caso o nome do arquivo seja o defindo no condicional if
         raise Exception # força um erro manualmente
except FileNotFoundError as e: # trata o erro e atribui o código de erro a uma variável
    print(e)
except Exception as e: # trata os erros de forma geral e atribui o erro a uma varíavel
    print('Error!')
else: # executa um código quando não há erro
    print(f.read())
    f.close()
finally: # Executa o código independentemente do resultado dos blocos try e except, porém executará também os blocos de exceção e else
    print("Executing Finally...\n")

try: #permite testar um bloco de códigos quanto aos erros
    f = open('currupt_file.txt') # tenta abrir o arquvio e caso ocorra um erro executa a exceção específica ou genéria na sequência de exceções
except FileNotFoundError as e: # trata o erro e atribui o código de erro a uma variável
    print(e)
except Exception as e: # trata os erros de forma geral e atribui o erro a uma varíavel
    print('Error!')
else: # executa um código quando não há erro
    print(f.readline(13))
    f.close()
finally: # Executa o código independentemente do resultado dos blocos try e except, porém executará também os blocos de exceção e else
    print("Executing Finally...")
