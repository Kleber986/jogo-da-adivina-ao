nota=0
nota1=0
nota2=0

nota=int(input("digite sua nota:.."))
nota1=int(input("digite sua nota1:"))
nota2=int(input("digite sua nota2:"))
media=((nota+nota1+nota2)/3)
if media >=6:
    print(media)
    print("parabes voce foi aprovado")
elif media<6:
    print(media)
    print("voce foi reprovado")
    print("voce esta de recuperacao")
    


