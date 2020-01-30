def gerador_NunsPseudoAleatorio(iteracoes):
    """esta funcao gera varios (de acordo com a iteracao do for) numeros pseudo-aleatorios entre 0 e 1, utilizando 3 variaveis e uma semente e retorna uma lista de valores pseudo aleatórios """
    a = 13
    c = 0
    M = 13033 #recomendado que seja primo

    #1 >= semente <= M 
    semente = 277
    x0 = semente
    xN = 0

    valores = []
    for i in range(iteracoes):
        #se for a primeira iteracao, calcula o primeiro termo da seq
        if i == 0:
            numSeq = (a * x0 + c) % M
        
        #senao, usa o termo anterior e continua a sequencia
        xN = numSeq
        numSeq = (a * xN + c) % M
        val_PseudoAleatorio = xN / M

        valores.append(val_PseudoAleatorio)
    
    return valores

def calIntegralDupla():
    xEnd = 1.
    yEnd = 14.

    numIteracoes = 188000
    resulIntegral = 0.

    x = gerador_NunsPseudoAleatorio(numIteracoes)
    y = gerador_NunsPseudoAleatorio(numIteracoes)
    for i in range(numIteracoes):
        x[i] = x[i] * xEnd
        y[i] = y[i] * yEnd

        #somando o resultado com a funcao
        resulIntegral += (x[i] * x[i]) + (2. * y[i] * y[i])   
        #outra funcao = (2. * x[i] * x[i] * x[i]) - (5. * y[i]) ==> 2x^3 - 5y - essa tem resultado negativo

    #multiplica os limite de integracao com o resultado e divido pelo numero de iteracoes
    resulIntegral = xEnd * yEnd * resulIntegral / numIteracoes
    
    return resulIntegral   

volume = calIntegralDupla()
print(volume)
