import random

print("#################################")
print("Bem vindo ao jogo de Adivinhação!")
print("#################################")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000


print("Qual nível de dificuldade?")
print("(1) - Fácil | (2) -  Médio | (3)  Difícil")

dificuldade = int(input("Escolha a dificuldade: "))

if(dificuldade == 1):
    total_de_tentativas = 20
elif(dificuldade == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#loop do jogo
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}.".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número ente 1 e 100: ")
    print("Você digitou:", chute_str)
    chute_int = int(chute_str)

    if(chute_int < 1 or chute_int > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    correto = numero_secreto == chute_int
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    if(correto):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou o número para cima!")
            print("Tente novamente.")
            print("#################################")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
        elif (menor):
            print("Você errou o número para baixo!")
            print("Tente novamente.")
            print("#################################")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

        pontos_perdidos = abs(numero_secreto - chute_int)
        pontos = pontos - pontos_perdidos