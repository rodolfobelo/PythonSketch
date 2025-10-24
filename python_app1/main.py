def verificar_par_ou_impar(numero):
    """
    Verifica se um número é par ou ímpar e exibe o resultado no terminal.
    """
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

# Exemplo de uso:
if __name__ == "__main__":
    try:
        entrada_usuario = input("Digite um número inteiro para verificar se é par ou ímpar: ")
        numero_digitado = int(entrada_usuario)
        verificar_par_ou_impar(numero_digitado)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
