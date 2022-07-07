import random

print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000
print('Qual nível de dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Defina a difículdade do jogo: '))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada,total_de_tentativas))
    chute = int(input('Digite um numero de 1 há 100: '))
    print('Você digitou ', chute)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100')
        continue

    acertou = chute == numero_secreto
    acima   = chute > numero_secreto
    abaixo  = chute < numero_secreto

    if (acertou):
        print('Parabéns! Você acertou.')
        break
    else:
        if(acima):
            print('O seu chute foi acima do que o numero secreto!')
        elif(abaixo):
            print('O seu chute foi abaixo do que o numero secreto!')

        rodada = rodada + 1

print('Fim de jogo.')

