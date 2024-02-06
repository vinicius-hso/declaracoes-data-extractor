# declaracoes-data-extractor

Aplicação destinada a extração de dados de declaraçõers de imposto de renda em arquivo PDF.

## preparando o ambiente

Instalar Python

[Link para instalação](https://www.python.org/downloads/)

Instalar Virtualenv

[Link para instaação](https://pypi.org/project/virtualenv/)

Criar ambiente virtual

> no diretorio raiz do projeto, crie um ambiente virtual

`virtualenv venv`

Ativar ambiente virtual

Windows: `.\venv\Scripts\activate`

MacOS: `source venv/bin/activate`

Instalar dependências

`pip install -r requirements.txt`

## executando aplicação

Na raiz do projeto execute o comando `python3 main.py`

Insira o caminho do diretório das declarações, um arquivo "relatorio.csv" será criado no diretório raiz da aplicação.

Exemplo:

> Insira o caminho do diretório de "Declarações": /Users/viniciusoliveira/Downloads/declaracoes
