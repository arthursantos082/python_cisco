# --- VARIÁVEIS ---

var = 1
print(var)

# Como usar uma variável?
var = 1
account_balance = 1000.0
client_name = 'Aluno UDF'
print(var, account_balance, client_name)
print(var)

# Observação: não dá pra usar uma variável que não existe
x = 1
# print(y)  # vai dar erro

# Concatenando variável e string
var = "3.8.5"
print("Versão Python: " + var)  # vírgula também serve

# Nota: não vamos ensinar a simplificação var = var + 1, então pularemos essa parte


# --- EXERCÍCIO PRÁTICO: SEGUNDOS EM HORAS ---

# Programa que calcula o número de segundos em um dado número de horas
# escrito há dois dias atrás

a = 2  # número de horas
seconds = 3600  # segundos em uma hora

print("Horas: ", a)  # imprimindo número de horas
print("Seconds in Hours: ", a * seconds)  # imprimindo número de segundos
print("Adeus")  # final do programa


# --- INTERAÇÃO COM O USUÁRIO ---

input()  # função famosa para receber input

print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")  # mostra o que o usuário digitou

# Versão simplificada:
anything = input("Conta-me qualquer coisa...")  # input já com texto
print("Hum...", anything, "...Realmente?")


# --- CONVERTENDO PARA FLOAT ---

# Recebendo números float
number = float(input("Digite um número Float: "))
print(number)


# --- BRINCANDO COM NÚMEROS E TEXTO (DESENHOS) ---

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
# resultado é legal kkkk


# --- INPUT E CONCATENAÇÃO DE STRINGS ---

# Observação: input() sempre retorna string
# Você pode concatenar strings usando o operador +
num_1 = input("Digite o primeiro número: ")  # exemplo: 12
num_2 = input("Digite o segundo número: ")   # exemplo: 21
print(num_1 + num_2)  # retorna 1221