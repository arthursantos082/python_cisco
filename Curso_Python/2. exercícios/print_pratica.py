# --- PRINT BÁSICO ---

print("Olá, Python!")
print("Como vai?")  # O Python pula a linha sozinho

# print(Isaque)  # Observação do erro do código

print()  # pode ser usado como "espaço entre linhas"
print("Como também pode ser usado\npara pular a linha")
print("\npara identação", "nós pode usar a", "vírgula pra isso")


# --- CONTROLE DE QUEBRA DE LINHA E SEPARAÇÃO ---

# mas se eu não quero que ele pule automático?
print("É só vc usar o", end="")
print(" 'end' que desta maneira eu não pulo linha")

# e se eu quero colocar algo nas identações?
print("Pra colocar", "alguma", "coisa", "nas", "identações", "basta", "colocar", sep="-")


# --- BRINCANDO COM PRINT (DESENHANDO COM TEXTO) ---

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

print("\ndobrou:\n")

print("        *        " * 2)
print("       * *       " * 2)
print("      *   *      " * 2)
print("     *     *     " * 2)
print("    *       *    " * 2)
print("   *         *   " * 2)
print("  *           *  " * 2)
print(" *             * " * 2)
print("******     ******" * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *******     " * 2)


# --- USANDO ASPAS E STRINGS ---

# Como usar ' no print?
print('I\'m Monty Python.')

# Pra printar número é só não colocar ""
print(1 + 1 * 2)

# sei que 2*3=6, mas como faz expoenciação?
print(2 ** 3)  # desta maneira foi feita a exponenciação


# --- TIPOS DE DIVISÃO E NÚMEROS ---

# sabia que tem como determinar um float?
print(6 / 3)    # ambos inteiros
print(6 / 3.)   # o segundo é float
print(6. / 3)   # o primeiro é float
print(6. / 3.)  # ambos são float

# Como faz divisão de número inteiro (divisão arredondada)?
print(6 // 3)  # fácil, né?

# Pra pegar o restante é básico
print(14 % 4)  # que é igual a 2

# Este exemplo é um pouco mais complicado:
print(12 % 4.5)

# Qual é o resultado?
# 3.0 → não 3 mas 3.0. A regra ainda funciona:
'''
12 // 4.5 dá 2.0,
2.0 * 4.5 dá 9.0,
12 - 9.0 dá 3.0.
'''