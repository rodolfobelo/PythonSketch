import sys
from mediaFinal import calcula_media, situacao_aluno


def run():
    try:
        assert calcula_media(8, 8) == 8
        assert calcula_media(5, 7) == 6

        msg, media = situacao_aluno(8, 8, 0)
        assert 'aprovado' in msg.lower()
        assert media == 8

        msg, media = situacao_aluno(8, 8, 10)
        assert 'falta' in msg.lower()

        msg, media = situacao_aluno(6, 6, 0, nota_recuperacao=6)
        assert 'aprovado' in msg.lower()
        assert abs(media - 6.0) < 1e-9

        msg, media = situacao_aluno(5.5, 5.5, 0, nota_recuperacao=4)
        assert 'reprovado' in msg.lower()

        msg, media = situacao_aluno(2, 2, 0)
        assert 'reprovado' in msg.lower()

    except AssertionError as e:
        print('Algum teste falhou:', e)
        sys.exit(1)
    except Exception as e:
        print('Erro nos testes:', e)
        sys.exit(2)
    print('Todos os testes passaram!')

if __name__ == '__main__':
    run()
