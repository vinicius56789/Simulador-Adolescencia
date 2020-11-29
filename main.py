from package import pessoais
from package import utilidades
from package import acoes

nome = utilidades.escreva('Qual seu nome? ')
classe = pessoais.financeiro()
idade = 13
qi = pessoais.qiInicial()
habilidadeEsportiva = pessoais.habilidadeEsportiva()
felicidade = pessoais.felicidade()
contaBancaria = 0
print('=' * 35)
print(f'\033[33m Bem vindo, {nome}, {idade} anos')
print(f'-> Sua classe social: {classe}')
print(f'-> Seu qi: {qi}')
print(f'-> Aptidão esportiva: {habilidadeEsportiva}')
print(f'-> Felicidade: {felicidade} \033[m')
print('=' * 35)
acoes.verificaIdade(idade, classe, qi, contaBancaria, habilidadeEsportiva, felicidade)


