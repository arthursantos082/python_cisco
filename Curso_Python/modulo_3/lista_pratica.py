# --- LISTAS EM PYTHON ---

# Lista = variável que guarda vários valores
# Cada elemento tem índice (posição) começando do 0
numbers = [10, 5, 7, 2, 1]
print(numbers)
print(numbers[0])  # primeiro elemento
print(numbers[-1]) # último elemento

# --- ALTERANDO ELEMENTOS ---
numbers[0] = 111      # muda o primeiro valor
numbers[1] = numbers[4]  # copia valor de outro índice
print(numbers)

# --- TAMANHO ---
print(len(numbers))  # len() → número de elementos

# --- REMOVENDO ELEMENTOS ---
del numbers[1]  # remove item específico
print(numbers)

# --- ADICIONANDO ELEMENTOS ---
numbers.append(99)      # adiciona no final
numbers.insert(1, 333)  # adiciona em posição específica
print(numbers)

# --- PERCORRENDO LISTAS ---
for n in numbers:
    print(n)  # itera sobre todos os elementos

# --- VIDA INTERIOR DAS LISTAS ---
# lista = endereço de memória, não valor direto
list_1 = [1]
list_2 = list_1  # list_2 e list_1 apontam pro mesmo lugar
list_1[0] = 2
print(list_2)  # [2] → muda junto!
# se quiser cópia independente, use slicing:

list_1 = [1]
list_2 = list_1[:]  # [:] copia o conteúdo
list_1[0] = 2
print(list_2)  # [1] → agora independente

# --- FATIAMENTO (SLICING) ---
# lista[início:fim] → do índice início até fim-1
my_list = [10, 8, 6, 4, 2]
print(my_list[1:3])   # [8,6]
print(my_list[:3])    # [10,8,6] → início 0
print(my_list[3:])    # [4,2] → até o final
print(my_list[:])     # copia toda a lista

# índices negativos funcionam também
print(my_list[1:-1])  # [8,6,4]

# --- DELETANDO FATIAS ---
del my_list[1:3]  # remove índices 1 e 2
print(my_list)    # [10,4,2]
del my_list[:]    # apaga conteúdo inteiro
print(my_list)    # []

# --- IN / NOT IN ---
# verifica se um valor está presente
my_list = ["A","B",1,2]
print("A" in my_list)      # True
print("C" not in my_list)  # True
print(2 not in my_list)    # False

# --- EXEMPLOS PRÁTICOS ---

# 1. MAIOR VALOR
nums = [17,3,11,5,1,9,7,15,13]
maior = nums[0]  # assumimos que o primeiro é o maior
for n in nums[1:]:  # percorremos o restante
    if n > maior:
        maior = n
print("Maior:", maior)

# 2. LOCALIZAR ELEMENTO
nums = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found = False
for i in range(len(nums)):
    if nums[i] == to_find:
        found = True
        break
if found:
    print("Elemento no índice:", i)
else:
    print("Não encontrado")

# 3. CONTAR OCORRÊNCIAS (ex: loteria)
drawn = [5,11,9,42,3,49]
bets = [3,7,11,42,34,49]
hits = 0
for n in bets:
    if n in drawn:
        hits += 1
print("Acertos:", hits)

# 4. REMOVER REPETIÇÕES
orig = [1,2,2,3,3,4,1]
clean = []
for n in orig:
    if n not in clean:
        clean.append(n)
print(clean)  # [1,2,3,4]

# --- LISTAS MULTIDIMENSIONAIS ---

# Listas bidimensionais → listas dentro de listas
# Exemplo: estação meteorológica com 24 horas por 31 dias
temps = [[0.0 for h in range(24)] for d in range(31)]  
# Linha = dia, Coluna = hora
# Inicializa toda a matriz com 0.0 (float)

# Temperatura média ao meio-dia
total = 0.0
for day in temps:  # day = cada linha da matriz
    total += day[11]  # coluna 11 = meio-dia
average = total / 31
print("Temperatura média ao meio-dia:", average)

# Maior temperatura do mês
highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("A maior temperatura foi:", highest)

# Contar dias com temperatura ao meio-dia >= 20°C
hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
print(hot_days, "dias estavam quentes.")

# --- LISTAS 3D (tridimensionais) ---
# Exemplo: hotel com 3 prédios, 15 andares, 20 quartos
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# False = quarto livre, True = ocupado

# Reservar quarto
rooms[1][9][13] = True  # 2º prédio, 10º andar, quarto 14

# Liberar quarto
rooms[0][4][1] = False  # 1º prédio, 5º andar, quarto 2

# Verificar vagas no 15º andar do 3º prédio
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print("Quartos disponíveis:", vacancy)

