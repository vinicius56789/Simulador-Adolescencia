import random
from package import pessoais
from package import utilidades


def verificaIdade(idade, classe, qi, dinheiro, habilidadeEsporte, felicidade):
    while idade <= 17:
        if classe == 'E':
            print(f'''Você chegou aos {idade} anos.
                    Devido sua classe social, você pode escolher:
                    [trabalhar] ganhe dinheiro para ajudar sua família
                    [esporte] jogue na rua''')
            classeE = utilidades.escreva('Qual quer fazer? ')
            while classeE != 'trabalhar' and classeE != 'esporte':
                print('''Apenas dentro das opções:
                    [trabalhar] ajude sua família
                    [esporte] jogue na rua''')
                classeE = utilidades.escreva('Escolha dentro das possibilidades: ')
            if classeE == 'trabalhar':
                dinheiro = trabalhar(dinheiro)
                dinheiro = dinheiro - (dinheiro * 0.9)
                felicidade = perdeFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            else:
                habilidadeEsporte = jogueNaRua(habilidadeEsporte)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
        elif classe == 'D':
            print(f'''Você chegou aos {idade} anos.
                    Devido sua classe social, você pode escolher:
                    [estudar] estudar em casa
                    [trabalhar] ganhe dinheiro
                    [esporte] jogue na rua''')
            classeD = utilidades.escreva('Qual quer fazer? ')
            while classeD != 'estudar' and classeD != 'trabalhar' and classeD != 'esporte':
                print('''Apenas dentro das opções:
                    [estudar] estudar em casa
                    [trabalhar] ganhe dinheiro
                    [esporte] jogue na rua''')
                classeD = utilidades.escreva('Escolha dentro das possibilidades: ')
            if classeD == 'estudar':
                qi = aumentaQi(qi)
                idade = pessoais.aniversario(idade)
            elif classeD == 'trabalhar':
                dinheiro = trabalhar(dinheiro)
                dinheiro = dinheiro - (dinheiro * 0.6)
                felicidade = perdeFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            else:
                habilidadeEsporte = jogueNaRua(habilidadeEsporte)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
        elif classe == 'C':
            print(f'''Você chegou aos {idade} anos.
                    Devido sua classe social, você pode escolher:
                    [estudar] estude num cursinho
                    [esporte] faça algum esporte
                    [trabalhar] ganhe dinheiro''')
            classeC = utilidades.escreva('Qual quer fazer? ')
            while classeC != 'estudar' and classeC != 'trabalhar' and classeC != 'esporte':
                print('''Apenas dentro das opções:
                    [estudar] estude num cursinho
                    [trabalhar] ganhe dinheiro
                    [esporte] faça algum esporte''')
                classeC = utilidades.escreva('Escolha dentro das possibilidades: ')
            if classeC == 'estudar':
                qi = aumentaQi(qi)
                idade = pessoais.aniversario(idade)
            elif classeC == 'trabalhar':
                dinheiro = trabalhar(dinheiro)
                dinheiro = dinheiro - (dinheiro * 0.2)
                felicidade = perdeFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            else:
                habilidadeEsporte = treinoEsportivo(habilidadeEsporte)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
        elif classe == 'B':
            print(f'''Você chegou aos {idade} anos.
                    Devido sua classe social, você pode escolher:
                    [estudar] estude num cursinho
                    [esporte] faça algum esporte
                    [trabalhar] ganhe dinheiro
                    [viajar] faça uma viagem''')
            classeB = utilidades.escreva('Qual quer fazer? ')
            while classeB != 'estudar' and classeB != 'trabalhar' and classeB != 'esporte' and classeB != 'viajar':
                print('''Apenas dentro das opções:
                    [estudar] estude num cursinho
                    [trabalhar] ganhe dinheiro
                    [esporte] faça algum esporte
                    [viajar] faça uma viagem''')
                classeB = utilidades.escreva('Escolha dentro das possibilidades: ')
            if classeB == 'estudar':
                qi = aumentaQiCursinho(qi)
                idade = pessoais.aniversario(idade)
            elif classeB == 'trabalhar':
                dinheiro = trabalhar(dinheiro)
                felicidade = perdeFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            elif classeB == 'esporte':
                habilidadeEsporte = treinoEsportivo(habilidadeEsporte)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            else:
                qi = aumentaQi(qi)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
        else:
            print(f'''Você chegou aos {idade} anos.
                                Devido sua classe social, você pode escolher:
                                [estudar] estude num cursinho
                                [esporte] faça algum esporte
                                [viajar] faça uma viagem''')
            classeA = utilidades.escreva('Qual quer fazer? ')
            while classeA != 'estudar' and classeA != 'esporte' and classeA != 'viajar':
                print('''Apenas dentro das opções:
                                [estudar] estude num cursinho
                                [trabalhar] ganhe dinheiro
                                [esporte] faça algum esporte
                                [viajar] faça uma viagem''')
                classeA = utilidades.escreva('Escolha dentro das possibilidades: ')
            if classeA == 'estudar':
                qi = aumentaQiCursinho(qi)
                idade = pessoais.aniversario(idade)
            elif classeA == 'esporte':
                habilidadeEsporte = treinoEsportivo(habilidadeEsporte)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
            else:
                qi = aumentaQi(qi)
                felicidade = ganharFelicidade(felicidade)
                idade = pessoais.aniversario(idade)
                print(f'''Faça sua segunda escolha.
                                Devido sua classe social, você pode escolher:
                                [estudar] estude num cursinho
                                [esporte] faça algum esporte
                                [viajar] faça uma viagem''')
                classeAA = utilidades.escreva('Qual quer fazer? ')
                while classeAA != 'estudar' and classeAA != 'esporte' and classeAA != 'viajar':
                    print('''Apenas dentro das opções:
                                [estudar] estude num cursinho
                                [trabalhar] ganhe dinheiro
                                [esporte] faça algum esporte
                                [viajar] faça uma viagem''')
                    classeAA = utilidades.escreva('Escolha dentro das possibilidades: ')
        print(f'Idade: {idade}, Qi: {qi}, Conta: {dinheiro}, Esportivo: {habilidadeEsporte}, Felicidade: {felicidade}')
    if idade == 18:
        print('Você genhou nos 18 anos: ')


def escola():
    sorteador = random.randint(0, 4)
    return sorteador


def aumentaQi(qi):
    qi = qi + escola()
    return qi


def cursinho():
    sorteador = random.randint(2, 10)
    return sorteador


def aumentaQiCursinho(qi):
    qi = qi + cursinho()
    return qi


def trabalhar(dinheiro):
    sorteador = random.randint(500, 750)
    saldo = dinheiro + sorteador
    return saldo


def treinoEsportivo(habilidade):
    sorteador = random.randint(5, 15)
    treino = habilidade + sorteador
    return treino


def jogueNaRua(habilidade):
    sorteador = random.randint(0, 10)
    treino = habilidade + sorteador
    return treino


def perdeFelicidade(felicidade):
    sorteador = random.randint(0, 2)
    felicidade = felicidade - sorteador
    return felicidade


def ganharFelicidade(felicidade):
    sorteador = random.randint(1, 3)
    if felicidade < 10:
        felicidade = felicidade + sorteador
    if felicidade > 10:
        felicidade = 10
    return felicidade