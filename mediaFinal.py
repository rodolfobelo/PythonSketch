n1 = float(input('Entre com a n1: '))
n2 = float(input('Entre com a n2: '))
faltas = int(input('Entre com a quantidade de faltas: '))
media = float((n1 + n2) / 2)


if(faltas >= 10):
    print('Você foi reprovado por falta!')
elif(media >= 7.0):
    print('Parabéns você foi aprovado.')
elif(media >= 5.0):
    print('Você se encontra de recuperação. /n Você terá uma nova chance.')
    nf = float(input('Entre com a nota de Recuperação: '))
    media = (media + nf) / 2
    if(media >= 6):
        print('Você foi aprovado!')
else:
    print('Você foi reprovado!')

print('Sua media é', media)