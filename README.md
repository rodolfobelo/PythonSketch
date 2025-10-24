# Documentação do Projeto PythonSketch

**Versão:** 1.0
**Data:** 24 de outubro de 2025

## 1. Visão Geral

O repositório `PythonSketch` é uma coleção de scripts desenvolvidos em Python, projetados para demonstrar funcionalidades básicas da linguagem e resolver problemas específicos de forma concisa. Cada script é autocontido e focado em uma única tarefa.

---

## 2. Descrição dos Módulos

A seguir, uma descrição detalhada de cada módulo presente neste projeto.

### 2.1. `mediaFinal.py`

- **Descrição:** Módulo interativo que calcula a média final de um aluno com base em duas notas e no número de faltas. O script implementa a lógica de aprovação, reprovação e recuperação, além de validar as entradas do usuário para garantir que as notas e faltas estejam dentro dos intervalos esperados.
- **Funcionalidades:**
    - Validação de entrada de dados (notas de 0 a 10, faltas não negativas).
    - Lógica de aprovação (média >= 7.0).
    - Lógica de recuperação (5.0 <= média < 7.0).
    - Lógica de reprovação (média < 5.0 ou faltas >= 10).
- **Execução:**
  ```powershell
  python .\mediaFinal.py
  ```

### 2.2. `mediaFinal_.py`

- **Descrição:** Uma versão simplificada do `mediaFinal.py`, oferecendo uma abordagem alternativa para o mesmo problema, sem a validação de entradas e a estrutura de funções.
- **Execução:**
  ```powershell
  python .\mediaFinal_.py
  ```

### 2.3. `variaveis.py`

- **Descrição:** Script de demonstração que ilustra a declaração e atribuição de uma variável em Python.
- **Execução:**
  ```powershell
  python .\variaveis.py
  ```

### 2.4. `teste.py`

- **Descrição:** Módulo básico que captura uma entrada de texto do usuário e a exibe no console. Serve como um exemplo fundamental de entrada e saída (I/O) em Python.
- **Execução:**
  ```powershell
  python .\teste.py
  ```

---

## 3. Como Utilizar

Para executar qualquer um dos scripts, certifique-se de ter o Python instalado em seu sistema. Navegue até o diretório do projeto via terminal e utilize o comando `python` seguido do nome do arquivo, conforme os exemplos acima.

---
