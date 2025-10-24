def verificar_par_ou_impar(numero):
    """
    Verifica se um número é par ou ímpar e retorna o resultado como uma string.
    """
    if numero % 2 == 0:
        return f"O número {numero} é PAR."
    else:
        return f"O número {numero} é ÍMPAR."
