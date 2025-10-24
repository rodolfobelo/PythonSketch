# Aplicação Verificador de Par ou Ímpar (ASP.NET Core MVC)

Esta é uma aplicação web simples construída com ASP.NET Core MVC em C# que permite ao usuário inserir um número inteiro e verificar se ele é par ou ímpar.

## Pré-requisitos

- [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) ou superior.

## Como Executar

1. **Clone o repositório** (se aplicável) ou certifique-se de que todos os arquivos do projeto estão no mesmo diretório.

2. **Abra um terminal** na raiz do projeto (onde o arquivo `ParImparApp.csproj` está localizado).

3. **Execute o seguinte comando** para compilar e iniciar a aplicação:

   ```bash
   dotnet run
   ```

4. **Abra seu navegador** e acesse a URL fornecida no terminal (geralmente `http://localhost:5000` ou `https://localhost:5001`).

## Estrutura do Projeto

- `ParImparApp.csproj`: Arquivo de projeto C# que define as configurações e dependências.
- `Program.cs`: Ponto de entrada da aplicação, onde o servidor web é configurado.
- `Controllers/`: Contém os controladores MVC.
  - `ParImparController.cs`: Lida com as requisições HTTP e a lógica de negócios.
- `Models/`: Contém os modelos de dados.
  - `NumberModel.cs`: Representa os dados da aplicação (o número de entrada e o resultado).
- `Views/`: Contém as views Razor (`.cshtml`).
  - `ParImpar/Index.cshtml`: A interface do usuário, com o formulário e a exibição do resultado.

## Próximos Passos

- **Adicionar Validação**: Implementar validação no lado do cliente (JavaScript) e no lado do servidor (Data Annotations no `NumberModel`) para uma melhor experiência do usuário.
- **Melhorar a UI**: Utilizar um framework CSS como Bootstrap para tornar a interface mais atraente.
- **Criar Testes Unitários**: Desenvolver testes para o `ParImparController` para garantir que a lógica de negócios funcione como esperado.
- **Publicar a Aplicação**: Usar o comando `dotnet publish` para preparar a aplicação para implantação em um servidor web como o IIS ou o Azure App Service.
