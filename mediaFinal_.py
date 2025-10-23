n1 = float(input('Entre com a n1: '))
n2 = float(input('Entre com a n2: '))
faltas = int(input('Entre com a quantidade de faltas: '))
media = (n1 + n2) / 2

if faltas >= 10:
    print('Sinto muito, você foi reprovado por falta!')
elif media >= 7.0:
    print('Parabéns, você foi aprovado.')
elif media >= 5.0:
    print('Você se encontra de recuperação.\nVocê terá uma nova chance.')
    nf = float(input('Entre com a nota de Recuperação: '))
    media = (media + nf) / 2
    if media >= 6.0:
        print('Parabéns, você foi aprovado!')
    else:
        print('Sinto muito, você foi reprovado!')
else:
    print('Sinto muito, você foi reprovado!')

print(f'Sua média é {media:.2f}')