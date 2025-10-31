# --- LISTAS EM PYTHON ---

# Uma lista guarda vários valores numa variável só
numbers = [10, 5, 7, 2, 1]
print(numbers)  # mostra tudo

# Índice começa em 0 (importante!)
print(numbers[0])  # primeiro elemento
print(numbers[-1]) # último elemento

# Dá pra alterar valores
numbers[0] = 111
numbers[1] = numbers[4]
print(numbers)

# Tamanho da lista → len()
print("Tamanho:", len(numbers))

# Apagar um item → del
del numbers[1]
print(numbers)

# --- ADICIONANDO ELEMENTOS ---

# append() → adiciona no final
numbers.append(99)

# insert() → insere onde quiser (índice, valor)
numbers.insert(1, 333)
print(numbers)

# lista vazia + for = lista preenchida
my_list = []
for i in range(5):
    my_list.append(i + 1)
print(my_list)

# --- PERCORRER LISTA ---

total = 0
for n in my_list:
    total += n
print("Soma:", total)

# --- INVERTENDO LISTA (jeito manual) ---
my_list = [10, 1, 8, 3, 5]
for i in range(len(my_list)//2):  # só metade da lista
    my_list[i], my_list[-i-1] = my_list[-i-1], my_list[i]
print("Invertida:", my_list)

# --- DICAS GERAIS ---

# [] → cria lista
# index → começa do 0
# len() → tamanho
# del → apaga elemento
# append() → adiciona no final
# insert() → adiciona onde quiser
# for → percorre cada item
# pode ter listas dentro de listas

# --- EXEMPLO FINAL ---

lst = [1, 2, 3]
lst.insert(1, 9)
lst.append(0)
del lst[0]
print(lst)  # [9, 2, 3, 0]
