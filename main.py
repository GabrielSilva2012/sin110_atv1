from dataclasses import field
from turtle import shape, width
from unittest import result
import numpy as np

# Função que le um arquivo txt e chama os dados que estao contidos, passando como parametro o nome do arquivo txt
def pegaMatriz(inst):
    nrows = []
    caminho = "C:/Users/gabri/Documents/algoritmos_grafos/arquivosMatriz/" + inst + '.txt'
    with open(caminho, 'rb') as f:
        #armazena em uma variavel a primeira linha do arquivo txt
        nrows = [int(field) for field in f.readline().split()]
        #armazena em uma variavel o restante da matriz passando como parametro o tamanho maximo de linhas
        dado = np.genfromtxt(f, dtype="int32", max_rows=len(nrows)) 
        #junta os dois arrays 
        result = np.vstack((nrows, dado))
    return result

pegaMatriz('exemplo')

# Função que salva em um novo arquivo o nome da instância e a dimensão da respectiva matriz
# com parametros passados anteriormente na funcao pega matriz
def salvaResultado(file):
    result = open("C:/Users/gabri/Documents/algoritmos_grafos/Resultados/" + file[0] + '.txt', "w" )
    a =  (str(file[0])  + ' ' +  str(file[1]))
    # armazena no arquivo os dados passados pela variavel 'a'
    result.writelines(a)
    result.close()
    return a

#parametro com nome do arquivo a ser acessado
nome_arquivo = 'ponte'
resultado = pegaMatriz(nome_arquivo)

# lista criada para armazenamentos de dados que serao utilizados na funcao salvaResultado
arquivo = []
arquivo.append(nome_arquivo)
# funcao que exibe a quantidade de colunas e a quantidade de linhas da matriz
arquivo.append(resultado.shape)

print(salvaResultado(arquivo))
 
