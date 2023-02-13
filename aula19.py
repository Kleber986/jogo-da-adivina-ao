import random
import os
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("digite seu numero:"))
while(sorteado!=jogador):
    os.system('clear')
    if(sorteado>jogador):
        print("erro o numero e maior")
    elif(sorteado<jogador):
        print("erro o numero e menor")
    erros+=1 
    jogador=int(input("digite seu numero:"))
print("numero"+str(jogador)+"voce acertou em"+str(erros+1)+"tentativas10")
