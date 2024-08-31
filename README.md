# Previsão do Tempo - Documentação

## Descrição

Este projeto é uma aplicação web para previsão do tempo, utilizando Flask no backend e HTML/CSS/JavaScript no frontend. O sistema permite ao usuário selecionar um estado e uma cidade, e em seguida, buscar as previsões do tempo para a cidade selecionada.

## Estrutura do Frontend

O frontend é composto por um arquivo HTML que utiliza Bootstrap para estilização e jQuery para manipulação dinâmica do DOM. Abaixo estão detalhes sobre a estrutura e o funcionamento do código.

### Estrutura HTML

- **Cabeçalho (`<head>`):**
  - Referências aos estilos CSS do Bootstrap.
  - Scripts JavaScript necessários: Bootstrap e jQuery.

- **Corpo (`<body>`):**
  - **Logo:** Imagem centralizada representando o logo do aplicativo.
  - **Formulário de Seleção de Estado e Cidade:**
    - Dropdown (`<select>`) para selecionar o estado, populado dinamicamente com a lista de estados disponíveis.
    - Dropdown (`<select>`) para selecionar a cidade, populado com base no estado selecionado.
    - Botão para buscar a previsão do tempo para a cidade selecionada.
  - **Tabelas de Previsão:**
    - Tabela para exibir a previsão do tempo atual (data, condição, umidade, temperatura, vento).
    - Tabela para exibir a previsão do tempo para os próximos 15 dias (amanhecer, manhã, tarde, noite).

### Scripts JavaScript

- **Requisição de Cidades por Estado:**
  - **Evento `change` no dropdown de Estados:** Quando o estado é alterado, uma requisição AJAX busca as cidades do estado selecionado.
  - **Função `buscarCidades(estado)`:** Popula o dropdown de cidades com os dados recebidos da API.

- **Requisição de Previsão do Tempo:**
  - **Função `buscarPrevisao()`:**
    - Verifica se uma cidade foi selecionada e realiza uma requisição AJAX para buscar a previsão do tempo atual.
    - Preenche a tabela com os dados recebidos e chama a função `buscarPrevisao15Dias()`.

- **Requisição de Previsão de 15 Dias:**
  - **Função `buscarPrevisao15Dias()`:**
    - Verifica se uma cidade foi selecionada e realiza uma requisição AJAX para buscar a previsão estendida.
    - Preenche a tabela com as informações detalhadas por períodos do dia.

- **Funções de Conversão de Data:**
  - **`convertDateISOToDMA(date)`:** Converte uma data ISO (AAAA-MM-DD) para o formato DD/MM/AAAA.
  - **`convertDMAToDM(date)`:** Converte uma data no formato DD/MM/AAAA para DD/MM.

### Exemplo de Funcionamento

1. O usuário acessa a aplicação e seleciona um estado.
2. As cidades disponíveis naquele estado são carregadas automaticamente.
3. O usuário escolhe uma cidade e clica no botão "Buscar previsão".
4. A previsão atual e a previsão para os próximos 15 dias são exibidas em suas respectivas tabelas.

## Instruções de Uso

1. **Configuração:** Certifique-se de que o Flask e as dependências estão corretamente instalados.
2. **Execução:** Inicie o servidor Flask para rodar a aplicação.
3. **Acesso:** Acesse a aplicação pelo navegador no endereço `http://127.0.0.1:5000`.

___


# Configuração do Projeto

Para que o projeto funcione corretamente, é necessário criar um arquivo de configuração chamado config.json na raiz do projeto. Este arquivo deve conter as seguintes configurações:

```json
{
    "host": "SEU_HOST",
    "user": "SEU_USUARIO",
    "password": "SUA_SENHA",
    "port": 3306,
    "database": "SEU_DATABASE",
    "token": "SEU_TOKEN"
}
```
### Descrição dos Campos
- host: O endereço do servidor de banco de dados.
- user: O nome de usuário para acessar o banco de dados.
- password: A senha para o usuário do banco de dados.
- port: A porta na qual o banco de dados está escutando. (Geralmente 3306 para MySQL)
- database: O nome do banco de dados que será utilizado.
- token: O token de autenticação para acessar a API do Climatempo.

### Obtendo o Token
O token pode ser obtido acessando o [Climatempo Advisor](https://advisor.climatempo.com.br/home/#!/tokens) e seguindo as instruções para gerar um novo token de API.

## Observações
Segurança: Certifique-se de manter o arquivo config.json fora do controle de versão para proteger informações sensíveis. Adicione-o ao .gitignore se ainda não estiver lá.
Validação: Verifique se as credenciais e o token estão corretos para garantir a comunicação adequada com o banco de dados e a API.


