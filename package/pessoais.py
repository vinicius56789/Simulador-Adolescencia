import time
import random


def financeiro():
    classe = ""
    social = ['E', 'D', 'C', 'B', 'A']
    sorteador = random.randint(1, 100)
    if sorteador <= 1:
        classe = social[4]
    elif 1 < sorteador <= 5:
        classe = social[3]
    elif 5 < sorteador <= 14:
        classe = social[2]
    elif 14 < sorteador <= 54:
        classe = social[1]
    elif 54 < sorteador <= 100:
        classe = social[0]
    return classe


def qiInicial():
    sorteador = random.randint(13, 40)
    return sorteador


def habilidadeEsportiva():
    sorteador = random.randint(0, 10)
    habilidade = sorteador
    return habilidade


def felicidade():
    alegria = 10
    return alegria


def ContaBanco(classe):
    if classe == 'E':
        saldo = -500
        return saldo
    elif classe == 'D':
        saldo = 0
        return saldo
    elif classe == 'C':
        saldo = 500
        return saldo
    elif classe == 'B':
        saldo = 10000
        return saldo
    elif classe == 'A':
        saldo = 100000
        return saldo


def dormir():
    time.sleep(5)


def aniversario(idade):
    idade += 1
    return idade





