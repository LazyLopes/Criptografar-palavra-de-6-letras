import numpy

Resposta = int(input(
                 "\n---------------------------------------------------\n"
                 "OBS: Todas as matrizes desse código são preechidas\n"
                 "na ordem de coluna por coluna!!!\n"
                 "---------------------------------------------------\n"
                 "A mensagem deve ter até 6 caracteres\n"
                 "---------------------------------------------------\n"
                 "Se você quer criptografar uma matriz 3x2\n"
                 "digite 1\n"
                 "Se você quer DEScriptografar uma matriz 3x2\n"
                 "digite 2\n"
                 ">>> "))



# MODULO DE CRIPTOGRAFIA
if Resposta == 1:
    # transforma a string em matriz
    def string_para_matriz(string):
        string += ' ' * (6 - len(string))
        matriz = [[0 for _ in range(2)] for _ in range(3)]
        for i, char in enumerate(string):
            linha = i % 3
            coluna = i // 3
            matriz[linha][coluna] = char
        return matriz
    
    string = input("Digite uma palavra com até 6 caracteres:\n"
                   ">>> ")
    string = string.upper()
    matriz = string_para_matriz(string)
    
    print("-------------------------------------")
    # transformando letra em numero
    def codificar_letra(letra):
        if letra == '':
            return 0
        else:
            return ord(letra) - ord('A') + 1


    matriz_codificada = [[0 for _ in range(2)] for _ in range(3)]
    for coluna in range(2):
        for linha in range(3):
            n = codificar_letra(matriz[linha][coluna])
            matriz_codificada[linha][coluna] = n

    print("Matriz original:")
    for linha in matriz:
        print(linha)

    print("\nMatriz codificada:")
    for linha in matriz_codificada:
        print(linha)

    # MATRIZ DE CRIPTOGRAFIA
    matriz_de_criptografia_3x3 = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 2, -1]
    ]

    # MULTIPLICANDO AS MATRIZES
    def multiplicar_matrizes(A, B):
        linhas_A = len(A)
        colunas_A = len(A[0])
        linhas_B = len(B)
        colunas_B = len(B[0])
    
        matriz_criptografada = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]
        for i in range(linhas_A):
            for j in range(colunas_B):
                for k in range(colunas_A):
                    matriz_criptografada[i][j] += A[i][k] * B[k][j]
    
        return matriz_criptografada

    matriz_criptografada = multiplicar_matrizes(matriz_de_criptografia_3x3, matriz_codificada)

    print("\nMatriz criptografada:")
    for linha in matriz_criptografada:
       print(linha)
       
    print("\nMensagem criptografada:")
    codigo = []
    for linha in matriz_criptografada:
        for coluna in range(1):
            codigo.append(linha[0])
    for linha in matriz_criptografada:
        for coluna in range(1):
            codigo.append(linha[1])
    for linha in codigo:
        print(linha, end=' ')   

# MODULO DE DESCRIPTOGRAFIA
elif Resposta == 2:
    matriz = [[0 for _ in range(2)] for _ in range(3)]

    numeros_string = input(f"Digite a mensagem criptografada: ")
    numeros_lista = list(map(int, numeros_string.split()))
    
    for i in range(3):
        for j in range(2):
            matriz[i][j] = numeros_lista[i + j * 3]
            
    # MATRIZ DE CRIPTOGRAFIA
    matriz_de_criptografia_3x3 = numpy.array([
        [1, 0, 1],
        [1, 1, 1],
        [0, 2, -1]
        ])
    
    # MATRIZ INVERSA
    matriz_de_DEScriptografia_3x3 = numpy.linalg.inv(matriz_de_criptografia_3x3)
    
    
    # MULTIPLICANDO AS MATRIZES
    def multiplicar_matrizes(A, B):
        linhas_A = len(A)
        colunas_A = len(A[0])
        linhas_B = len(B)
        colunas_B = len(B[0])
    
        matriz_DEScriptografada = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]
        for i in range(linhas_A):
            for j in range(colunas_B):
                for k in range(colunas_A):
                    matriz_DEScriptografada[i][j] += A[i][k] * B[k][j]
    
        return matriz_DEScriptografada

    matriz_DEScriptografada = multiplicar_matrizes(matriz_de_DEScriptografia_3x3, matriz)

    def matriz_float_para_int(matriz_float):
        matriz_int = []
        for linha_float in matriz_float:
            linha_int = [int(valor) for valor in linha_float]
            matriz_int.append(linha_int)
        return matriz_int
    
    matriz_DEScriptografada = matriz_float_para_int(matriz_DEScriptografada)
    
    print("\nMatriz DEScriptografada:")
    for linha in matriz_DEScriptografada:
       print(linha)
       
    # transformando numero em letra
    def codificador_numero(numero):
        if numero == 0:
            return ' '
        elif 1 <= numero and numero <= 26:
            return chr(numero + ord('A') - 1)
        
    def matriz_numeros_para_letras(matriz_numeros):
        matriz_letras = []
        for linha in matriz_numeros:
            linha_letras = [codificador_numero(numero) for numero in linha]
            matriz_letras.append(linha_letras)
        return matriz_letras
    
    matriz_DEScodificada = matriz_numeros_para_letras(matriz_DEScriptografada)
    
    # corrigindo erro se aparecer um 'None' na matriz
    for i in range(len(matriz_DEScodificada)):
        for j in range(len(matriz_DEScodificada[i])):
            if matriz_DEScodificada[i][j] is None:
                matriz_DEScodificada[i][j] = " "
    
    # transformando matriz em string
    string_matriz = ''
    for col in range(len(matriz_DEScodificada[0])):
        for linha in matriz_DEScodificada:
            string_matriz += str(linha[col])
    
    string_matriz = string_matriz.strip()

    print(f"\nSua mensagem é '{string_matriz}'")

else:
    print("\nDigite somente 1 ou 2\n")