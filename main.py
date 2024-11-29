#julio cesar silva rodrigues palma francisco
import random

def jogo_adivinhacao():
    print("jogo da adivinhação!")
    print("Estou pensando em um número entre 1 e 10. Tente adivinhar qual é.")
#é um proseso que move codigos ou dados  
 
    numero_secreto = random.randint(1, 10)
    tentativas = 5
    acertou = False
#funcionais é aquele diz oq o codigo deve fazer, ja o nao funcional é aquele que avisa quando tem algo de errado
    while not acertou:

        palpite = input("Digite qual numero voce acha que é: ")
        
        if not palpite.isdigit():
            print("Por favor, coloque um numero entre 1 a 10!")
            continue
        
        palpite = int(palpite)
        tentativas += 1
        
        if palpite < numero_secreto:
            print("baixo demais, tente denovo.")
        elif palpite > numero_secreto:
            print("Muito alto, tente denovo.")
        else:
            print(f"Parabéns! voce falou o numero verdadeiro com {tentativas} tentativas.")
            acertou = True

jogo_adivinhacao()
