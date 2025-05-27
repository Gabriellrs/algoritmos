# 1. CRIAÇÃO de uma lista (array)
print("--- 1. Criação ---")
# Podemos criar uma lista vazia ou com elementos iniciais
lista_numeros = [10, 20, 30, 40, 50]
lista_frutas = ["maçã", "banana", "laranja"]
lista_vazia = []

print(f"Lista de números: {lista_numeros}")
print(f"Lista de frutas: {lista_frutas}")
print(f"Lista vazia: {lista_vazia}\n")


# 2. LEITURA / ACESSO a elementos por índice
print("--- 2. Acesso a Elementos ---")
# Lembre-se que o índice começa em 0
primeiro_numero = lista_numeros[0]
segunda_fruta = lista_frutas[1]
ultimo_numero = lista_numeros[-1] # Python permite índices negativos para contar do fim

print(f"Primeiro número: {primeiro_numero}") # Saída: 10
print(f"Segunda fruta: {segunda_fruta}")   # Saída: banana
print(f"Último número (usando índice -1): {ultimo_numero}") # Saída: 50
# Tentar acessar um índice que não existe resultará em um erro (IndexError)
# print(lista_numeros[10]) # Descomente para ver o erro
print("")


# 3. ATUALIZAÇÃO de um elemento
print("--- 3. Atualização de Elementos ---")
print(f"Lista de frutas antes da atualização: {lista_frutas}")
lista_frutas[1] = "morango" # Atualiza o elemento no índice 1
print(f"Lista de frutas depois da atualização: {lista_frutas}") # Saída: ['maçã', 'morango', 'laranja']
print("")


# 4. TAMANHO da lista
print("--- 4. Tamanho da Lista ---")
tamanho_numeros = len(lista_numeros)
tamanho_frutas = len(lista_frutas)
print(f"A lista de números tem {tamanho_numeros} elementos.") # Saída: 5
print(f"A lista de frutas tem {tamanho_frutas} elementos.")   # Saída: 3
print("")


# 5. INSERÇÃO de elementos
print("--- 5. Inserção de Elementos ---")
# Adicionar ao final da lista (append)
print(f"Lista de números antes do append: {lista_numeros}")
lista_numeros.append(60)
print(f"Lista de números depois do append(60): {lista_numeros}") # Saída: [10, 20, 30, 40, 50, 60]

# Inserir em uma posição específica (insert)
# insert(indice, valor)
print(f"Lista de frutas antes do insert: {lista_frutas}")
lista_frutas.insert(1, "abacaxi") # Insere "abacaxi" no índice 1
print(f"Lista de frutas depois do insert(1, 'abacaxi'): {lista_frutas}") # Saída: ['maçã', 'abacaxi', 'morango', 'laranja']
print("")


# 6. REMOÇÃO de elementos
print("--- 6. Remoção de Elementos ---")
# Remover pelo índice (pop) - retorna o elemento removido
print(f"Lista de números antes do pop: {lista_numeros}")
elemento_removido = lista_numeros.pop(2) # Remove o elemento no índice 2 (que é 30)
print(f"Elemento removido com pop(2): {elemento_removido}")
print(f"Lista de números depois do pop(2): {lista_numeros}") # Saída: [10, 20, 40, 50, 60]

# Se não passar índice para pop(), remove o último elemento
ultimo_elemento_removido = lista_numeros.pop()
print(f"Elemento removido com pop() (último): {ultimo_elemento_removido}") # Era 60
print(f"Lista de números depois do pop(): {lista_numeros}") # Saída: [10, 20, 40, 50]

# Remover pela primeira ocorrência do valor (remove)
print(f"Lista de frutas antes do remove: {lista_frutas}") # ['maçã', 'abacaxi', 'morango', 'laranja']
lista_frutas.remove("morango")
print(f"Lista de frutas depois do remove('morango'): {lista_frutas}") # Saída: ['maçã', 'abacaxi', 'laranja']
# Se o elemento a ser removido não existir, dará um erro (ValueError)
# lista_frutas.remove("uva") # Descomente para ver o erro

# Remover usando del (por índice)
print(f"Lista de números antes do del: {lista_numeros}") # [10, 20, 40, 50]
del lista_numeros[0] # Remove o elemento no índice 0
print(f"Lista de números depois do del lista_numeros[0]: {lista_numeros}") # Saída: [20, 40, 50]
print("")


# 7. BUSCA por um elemento
print("--- 7. Busca por Elementos ---")
# Verificar se um elemento existe na lista (operador 'in')
tem_laranja = "laranja" in lista_frutas
tem_uva = "uva" in lista_frutas
print(f"A lista de frutas contém 'laranja'? {tem_laranja}") # Saída: True
print(f"A lista de frutas contém 'uva'? {tem_uva}")     # Saída: False

# Encontrar o índice da primeira ocorrência de um elemento (index)
try:
    indice_abacaxi = lista_frutas.index("abacaxi")
    print(f"O índice de 'abacaxi' é: {indice_abacaxi}") # Saída: 1
except ValueError:
    print("'abacaxi' não encontrado na lista.")

try:
    indice_uva = lista_frutas.index("uva")
    print(f"O índice de 'uva' é: {indice_uva}")
except ValueError:
    print("'uva' não foi encontrada na lista de frutas.") # Esta mensagem será impressa
print("")


# 8. PERCORRER / ITERAR sobre os elementos da lista
print("--- 8. Percorrer/Iterar ---")
print("Frutas na lista:")
for fruta in lista_frutas:
    print(f"- {fruta}")

print("\nNúmeros na lista e seus quadrados:")
for numero in lista_numeros:
    print(f"Número: {numero}, Quadrado: {numero * numero}")
print("")

# Outras operações úteis:
print("--- Outras Operações Úteis ---")
# Contar ocorrências de um elemento
lista_contagem = [1, 2, 2, 3, 2, 4, 2]
contagem_de_2 = lista_contagem.count(2)
print(f"Lista para contagem: {lista_contagem}")
print(f"O número 2 aparece {contagem_de_2} vezes.") # Saída: 4

# Ordenar uma lista (in-place, modifica a lista original)
lista_para_ordenar = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista antes de ordenar: {lista_para_ordenar}")
lista_para_ordenar.sort()
print(f"Lista depois de .sort(): {lista_para_ordenar}")

# Ordenar uma lista (criando uma nova lista ordenada)
outra_lista_para_ordenar = [50, 10, 80, 20]
print(f"Outra lista original: {outra_lista_para_ordenar}")
lista_ordenada_nova = sorted(outra_lista_para_ordenar)
print(f"Nova lista ordenada com sorted(): {lista_ordenada_nova}")
print(f"Outra lista original (não modificada): {outra_lista_para_ordenar}")

# Reverter uma lista (in-place)
lista_para_reverter = [1, 2, 3, 4, 5]
print(f"Lista antes de reverter: {lista_para_reverter}")
lista_para_reverter.reverse()
print(f"Lista depois de .reverse(): {lista_para_reverter}")