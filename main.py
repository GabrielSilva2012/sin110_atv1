from dataclasses import field
from turtle import shape, width
from unittest import result
import numpy as np

def pegaMatriz(inst):
    nrows = []
    caminho = "C:/Users/gabri/Documents/algoritmos_grafos/arquivosMatriz/" + inst + '.txt'
    with open(caminho, 'rb') as f:
        nrows = [int(field) for field in f.readline().split()]
        dado = np.genfromtxt(f, dtype="int32", max_rows=len(nrows)) 
        result = np.vstack((nrows, dado))
    return result

def salvaResultado(arquivo):
    result = open("C:/Users/gabri/Documents/algoritmos_grafos/Resultados/" + arquivo[0] + '.txt', "w" )
    result.writelines('Nome do Arquivo: '+ str(arquivo[0]) + '\n'+ 'Dimensao da Matriz: '+ str(arquivo[1]) )
    result.close()

nome_arquivo = 'ponte'
resultado = pegaMatriz(nome_arquivo)

arquivo = []
arquivo.append(nome_arquivo)
arquivo.append(resultado.shape)

salvaResultado(arquivo)
