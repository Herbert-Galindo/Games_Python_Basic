import random


def jogar():

    print("Bem vindo ao jogo de advinhação!\n")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade que você deseja?")

    nivel = int(input("(1) Fácil (2) Médio (3) Difícil: \n"))


    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    while(rodada <= tentativas):
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input("Digite o numero secreto que deve ser entre 1 e 100: \n"))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou! E fez: {pontos} pontos!")
            break
        else:
            if(chute_maior):
                print("O numero secreto é menor que: ", chute)
            elif(chute_menor):
                print("O numero secreto é maior que: ", chute)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Game Over")

if(__name__=="__main__"):
    jogar()