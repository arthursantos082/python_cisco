# --- OPERADORES BÁSICOS ---

# =  → atribuição (coloca valor na variável)
# == → comparação (verifica se os valores são iguais)
var = 0
print(var == 0)  # True
var = 1
print(var == 0)  # False

# Outros operadores:
# >  maior que
# <  menor que
# >= maior ou igual
# <= menor ou igual
n = int(input("Digite um número: "))
print(n >= 100)


# --- ESTRUTURAS CONDICIONAIS (if, elif, else) ---

# if = se / else = senão / elif = mas se
if True:
    print("Condição verdadeira")
else:
    print("Condição falsa")

# Exemplo:
sheep_counter = 120
if sheep_counter >= 120:
    print("Dormindo... 💤")

# if / elif / else:
'''if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()'''

# Comparando dois números:
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

if n1 > n2:
    maior = n1
else:
    maior = n2
print("Maior número:", maior)

# Comparando três números:
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print("Maior número:", maior)


# --- OPERADORES LÓGICOS ---

# and → True se ambos forem verdadeiros
# or  → True se pelo menos um for verdadeiro
# not → inverte o valor lógico

x, y = 10, 5
print(x > 0 and y > 0)  # True
print(x > 0 or y < 0)   # True
print(not (x > y))      # False


# --- OPERADORES BIT A BIT (bitwise) ---

# Trabalham diretamente com bits (0 e 1)
x = 15  # 0000 1111
y = 16  # 0001 0000

print(x & y)  # E bit a bit → 0
print(x | y)  # OU bit a bit → 31
print(~x)     # NÃO bit a bit → -16  (usa complemento de dois)
print(x ^ y)  # XOR (diferentes) → 31

# Deslocamento de bits (shift)
print(y >> 1)  # direita → divide por 2 → 8
print(y << 3)  # esquerda → multiplica por 2³ → 128

# Complemento de dois:
# ~x = -(x + 1)
# Ex: x=15 → ~x = -16
