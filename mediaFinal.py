"""
Script interativo para avaliar a situação escolar de um aluno com base em duas notas e
quantidade de faltas.
Fluxo:
- Solicita ao usuário duas notas (n1, n2) como floats e a quantidade de faltas como int.
- Calcula a média simples inicial: media = (n1 + n2) / 2.
- Se faltas >= 10: o aluno é reprovado por falta.
- Senão, avalia pela média:
    - media >= 7.0: aprovado.
    - 5.0 <= media < 7.0: entra em recuperação — solicita a nota de recuperação (nf),
      recalcula media_final = (media + nf) / 2; se media_final >= 6.0: aprovado, senão reprovado.
    - media < 5.0: reprovado.
- Ao final imprime a média final (ou média inicial caso não haja recuperação).
Efeitos colaterais:
- Realiza entradas via input() e exibe mensagens com print().
- Pode lançar ValueError se o usuário digitar valores não numéricos.
- Observação: a mensagem de recuperação no código contém '/n' em vez de '\n' para quebra de linha.
Retorno:
- Não retorna valor (None); apenas interage com o usuário e exibe resultados.
"""

def calcula_media(n1: float, n2: float) -> float:
    """Retorna a média simples entre duas notas."""
    return (n1 + n2) / 2


def situacao_aluno(n1: float, n2: float, faltas: int, nota_recuperacao: float | None = None) -> tuple[str, float]:
    """Determina a situação do aluno e retorna uma tupla (mensagem, media_final).

    Regras:
    - Se faltas >= 10: reprovado por falta (média final é a média inicial)
    - Se media >= 7.0: aprovado
    - Se 5.0 <= media < 7.0: recuperação — se for fornecida `nota_recuperacao`, recalcula
      media_final = (media + nota_recuperacao) / 2 e decide aprovação (media_final >= 6.0)
    - Se media < 5.0: reprovado
    """
    if n1 < 0 or n2 < 0 or faltas < 0:
        raise ValueError('Notas e faltas devem ser não-negativas')

    media = calcula_media(n1, n2)
    media_final = media

    if faltas >= 10:
        return ('Sinto muito, você foi reprovado por falta!', media_final)

    if media >= 7.0:
        return ('Parabéns, você foi aprovado.', media_final)

    if media >= 5.0:
        # recuperação
        if nota_recuperacao is None:
            return ('Você se encontra de recuperação. Forneça a nota de recuperação.', media_final)
        media_final = (media + nota_recuperacao) / 2
        if media_final >= 6.0:
            return ('Parabéns, você foi aprovado!', media_final)
        else:
            return ('Sinto muito, você foi reprovado!', media_final)

    return ('Sinto muito, você foi reprovado!', media_final)


def le_float(prompt: str, min_value: float = None, max_value: float = None) -> float:
    while True:
        try:
            v = float(input(prompt))
        except ValueError:
            print('Entrada inválida. Digite um número.')
            continue
        if min_value is not None and v < min_value:
            print(f'Valor deve ser >= {min_value}.')
            continue
        if max_value is not None and v > max_value:
            print(f'Valor deve ser <= {max_value}.')
            continue
        return v


def le_int(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            v = int(input(prompt))
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
            continue
        if min_value is not None and v < min_value:
            print(f'Valor deve ser >= {min_value}.')
            continue
        return v


if __name__ == '__main__':
    n1 = le_float('Entre com a n1 (0-10): ', 0, 10)
    n2 = le_float('Entre com a n2 (0-10): ', 0, 10)
    faltas = le_int('Entre com a quantidade de faltas: ', 0)

    media = calcula_media(n1, n2)

    if 5.0 <= media < 7.0 and faltas < 10:
        print('Você se encontra de recuperação.\nVocê terá uma nova chance.')
        nf = le_float('Entre com a nota de Recuperação (0-10): ', 0, 10)
        msg, media_final = situacao_aluno(n1, n2, faltas, nota_recuperacao=nf)
        print(msg)
    else:
        msg, media_final = situacao_aluno(n1, n2, faltas)
        print(msg)

    print(f'Sua média é {media_final:.2f}')