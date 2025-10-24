from flask import Flask, request, render_template_string
from utils import verificar_par_ou_impar

app = Flask(__name__)

# Template HTML simples para o formulário e resultado
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verificador de Par ou Ímpar</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { margin-bottom: 20px; }
        input[type="number"] { padding: 8px; margin-right: 10px; }
        input[type="submit"] { padding: 8px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        input[type="submit"]:hover { background-color: #45a049; }
        .resultado { font-size: 1.2em; font-weight: bold; color: #333; }
        .erro { color: red; }
    </style>
</head>
<body>
    <h1>Verificador de Par ou Ímpar</h1>
    <form action="/verificar" method="post">
        <label for="numero">Digite um número inteiro:</label>
        <input type="number" id="numero" name="numero" required>
        <input type="submit" value="Verificar">
    </form>

    {% if resultado %}
        <p class="resultado">{{ resultado }}</p>
    {% endif %}
    {% if erro %}
        <p class="erro">{{ erro }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, resultado=None, erro=None)

@app.route('/verificar', methods=['POST'])
def verificar():
    if request.method == 'POST':
        try:
            numero_str = request.form['numero']
            numero = int(numero_str)
            resultado = verificar_par_ou_impar(numero)
            return render_template_string(HTML_TEMPLATE, resultado=resultado, erro=None)
        except ValueError:
            erro = "Entrada inválida. Por favor, digite um número inteiro."
            return render_template_string(HTML_TEMPLATE, resultado=None, erro=erro)
    return index() # Redireciona para a página inicial se não for POST

if __name__ == '__main__':
    app.run(debug=True)