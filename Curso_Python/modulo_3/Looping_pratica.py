# --- LOOPS EM PYTHON ---

# 1. LOOP WHILE
# Executa instruções enquanto a condição for True
counter = 5
while counter > 0:
    print("Dentro do loop:", counter)
    counter -= 1
print("Fora do loop:", counter)

# Estrutura geral
'''
while condição:
    instrução_1
    instrução_2
    ...
    instrução_n
# O corpo do loop deve alterar a condição para evitar loop infinito
'''

# Exemplo de loop infinito
# while True:
#     print("Preso em um loop infinito!")

# Exemplo prático: encontrar o maior número
largest_number = -999999999
number = int(input("Digite um número ou -1 para parar: "))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Digite um número ou -1 para parar: "))
print("O maior número é:", largest_number)

# Contando pares e ímpares
odd_numbers = 0
even_numbers = 0
number = int(input("Digite um número ou 0 para parar: "))
while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Digite um número ou 0 para parar: "))
print("Ímpares:", odd_numbers, "Pares:", even_numbers)

# Usando variável como condição
counter = 5
while counter:
    print("Dentro do loop:", counter)
    counter -= 1
print("Fora do loop:", counter)

# --- LAB: adivinhe o número secreto ---
# while number != secret_number:
#     print("Ha ha! Você está preso no loop!")
#     number = int(input("Digite um número: "))
# print("Muito bem, trouxa! Você está livre agora.")

# --- LOOP FOR ---
# Itera sobre uma sequência de valores
for i in range(5):
    print("Valor de i:", i)

# range() pode ter 1, 2 ou 3 argumentos
# range(stop)
for i in range(3):  # 0,1,2
    print(i, end=" ")
print()

# range(start, stop)
for i in range(2, 8):  # 2,3,4,5,6,7
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(6, 1, -2):  # 6,4,2
    print(i, end=" ")
print()

# Exemplo: primeiros poderes de 2
for expo in range(5):  # 0 a 4
    print(2 ** expo)

# LAB: "contando Mississipi"
import time
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
print("Pronto ou não, aqui vou eu!")

# --- BREAK E CONTINUE ---
# break → sai do loop imediatamente
for letter in "OpenEDG Python":
    if letter == "P":
        break
    print(letter, end="")
print()

# continue → pula para próxima iteração
for letter in "pyxpyxpyx":
    if letter == "x":
        continue
    print(letter, end="")
print()

# Exemplo: remover vogais (continue)
user_word = "abstemious".upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

# --- ELSE EM LOOPS ---
# Executa se o loop terminar normalmente (sem break)
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

for i in range(3):
    print(i)
else:
    print(i, "else")


