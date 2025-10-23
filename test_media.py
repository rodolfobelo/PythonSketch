from mediaFinal import calcula_media, situacao_aluno


def test_calcula_media():
    assert calcula_media(8, 8) == 8
    assert calcula_media(5, 7) == 6


def test_aprovado_direto():
    msg, media = situacao_aluno(8, 8, 0)
    assert 'aprovado' in msg.lower()
    assert media == 8


def test_reprovado_por_falta():
    msg, media = situacao_aluno(8, 8, 10)
    assert 'falta' in msg.lower()


def test_recuperacao_aprovada():
    # média inicial 6 -> recuperação com nf=6 garante média_final = 6 -> aprovado
    msg, media = situacao_aluno(6, 6, 0, nota_recuperacao=6)
    assert 'aprovado' in msg.lower()
    assert abs(media - 6.0) < 1e-9


def test_recuperacao_reprovada():
    # média inicial 5.5 -> recuperação com nf=4 -> media_final = (5.5+4)/2 = 4.75 -> reprovado
    msg, media = situacao_aluno(5.5, 5.5, 0, nota_recuperacao=4)
    assert 'reprovado' in msg.lower()


def test_reprovado_direto():
    msg, media = situacao_aluno(2, 2, 0)
    assert 'reprovado' in msg.lower()
