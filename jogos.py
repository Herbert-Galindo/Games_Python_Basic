import advinhacao
import forca

def escolha_jogo():

    print("Qual jogo deseja jogar? \n")

    jogo = int(input("(1) jogo da Forca (2) Jogo de Advinhação\n"))

    if(jogo == 1):
        print("Jogando Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Jogo de Advinhação")
        advinhacao.jogar()
    else:
        print("Escolha um jogo válido")

if(__name__=="__main__"):
    escolha_jogo()