# Pergunta 1: O que acontece quando você tenta invocar uma função antes de defini-la? Exemplo:

hi()
 
def hi():
    print("hi!")
 
#Gera um NameError

# Pergunta 2: O que acontecerá quando você executar o código abaixo?

def hi():
    print("hi")
 
hi(5)
 
#Gera um TypeError (pois não leva argumentos)

# Pergunta 3: Qual é a saída do trecho de código?

def hi():
    return
    print("Oi!")
 
hi()
 
#Retorna none

# Pergunta 4: Qual é a saída do trecho de código?

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
 
print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
 
#''' True, False, None '''

# Pergunta 5: Qual é a saída do trecho de código?

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
 
print(even_num_lst(11))
 
#[0, 2, 4, 6, 8, 10]

#Pergunta 6: Qual é a saída do trecho de código?

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
 
#[1, 4, 9, 16, 25]

#Pergunta 7: Qual é a saída do trecho de código?

def message():
    alt = 1
    print("Olá Mundo!")
 
 
print(alt)
 
#NameError, alt não definido

#Pergunta 8: Qual é a saída do trecho de código?

a = 1
 
 
def fun():
    a = 2
    print(a)
 
 
fun()
print(a)
 
'''
2
1
'''

#Pergunta 9: Qual é a saída do trecho de código?

a = 1
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
fun()
a = 3
print(a)
 
'''
2
3
'''

#Pergunta 10: Qual é a saída do trecho de código?

a = 1
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
a = 3
fun()
print(a)
 
'''
2
2
'''

#Pergunta 11: O que irá acontecer se você tentar rodar o trecho de código a seguir e porque?
def factorial(n):
    return n * factorial(n - 1)
 
 
print(factorial(4))
 
#RecursionError: não possui terminação da condição

#Pergunta 12: Qual é a saída do trecho de código?
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
 
print(fun(25))
 
#56

#Pergunta 13: O que acontece quando você tenta executar o seguinte snippet?
my_tup = (1, 2, 3)
print(my_tup[2])
 
#3

#Pergunta 14: Qual é a saída do trecho de código?
tup = 1, 2, 3
a, b, c = tup
 
print(a * b * c)
 
#6

#Pergunta 14: Complete o código para usar corretamente o método count() para encontrar o número de duplicatas de 2 na seguinte tupla.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    

#Saídas: 4

#Pergunta 15: escreva um programa que junte os dois dicionários (d1 e d2) e crie um novo (d3).
d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#Pergunta 16: escreva um programa que converta a lista my_list em uma tupla.
my_list = ["car", "Ford", "flor", "Tulip"]

t = tuple(my_list)
print(t)

#Pergunta 17: escreva um programa que converta a tupla colors em um dicionário.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

#Pergunta 18: O que acontecerá quando você executar o código abaixo?
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
 
print(copy_my_dictionary)
 
#{'A': 1, 'B': 2}

#Pergunta 19: Qual é o resultado do programa a seguir?
colors = {
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "vermelho": (255, 0, 0),
    "verde": (0, 128, 0)
    }
 
for col, rgb in colors.items():
    print(col, ":", rgb)
 
'''
branco : (255, 255, 255)
cinza : (128, 128, 128)
vermelho : (255, 0, 0)
verde : (0, 128, 0)
'''

#Pergunta 20: Qual será o comportamento do programa a seguir quando o usuário entra com 0?
try:
    value = int(input("Entre um valor: "))
    print(value/value)
except ValueError:
    print("Entrada incorreta...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except:
    print("Booo!")
 
#"Entrada muito ruim..."

#Pergunta 21: Qual será o comportamento do programa a seguir quando o usuário entra com 0?
value = input("Entre um valor: ")
print(10/value)
 
#TypeError: não foi convertido em tipo inteiro (input normal se mantém em string)

