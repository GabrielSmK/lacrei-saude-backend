# Lacrei Saúde Backend

## Índice

* [Introdução](#introdução)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Instalação e Execução](#instalação-e-execução)
* [Execução de teste unitário](#execução-de-teste-unitário)

## Introdução

Esta é uma desenvolvida para gerenciar informações de profissionais de saúde e consultas médicas. Este projeto faz parte do projeto voluntário Lacrei Saúde, com foco especial na comunidade LGBTQIAPN+.

A API permite:
- Cadastro, atualização, consulta e remoção de profissionais de saúde
- Agendamento e gerenciamento de consultas médicas

## Tecnologias Utilizadas

### Poetry
Poetry foi escolhido para gerenciamento de dependências e empacotamento porque:
- Gerenciamento de dependências determinístico: Garante reprodutibilidade do ambiente.
- Fácil configuração de ambientes virtuais: Simplifica o processo de desenvolvimento.
- Gerenciamento de build: Facilita a distribuição do projeto, se necessário.

### FastAPI
FastAPI foi escolhido como o framework web principal devido a:
- Alta performance: Construído sobre Starlette e Pydantic, oferece um desempenho excepcional.
- Facilidade de uso: Sintaxe intuitiva e documentação automática da API.
- Tipagem estática: Reduz erros e melhora a manutenibilidade do código.
- Validação automática: Utiliza Pydantic para validação de dados de entrada e saída.

### SQLAlchemy
SQLAlchemy é nosso ORM (Object-Relational Mapping) de escolha porque:
- Flexibilidade: Suporta múltiplos bancos de dados com mínimas alterações no código.
- Poder e expressividade: Permite consultas complexas e otimizações de performance.
- Integração com FastAPI: Funciona bem com o ecossistema do FastAPI.

## Instalação e Execução

### Pré-requisitos
- Python 3.12+
- Poetry

#### 1. Instale o pipx

 ```
  py -m pip install --user pipx
  py -m pip install pipx
  py -m pipx ensurepath
  (Reinicie o Visual Studio)
  ```

#### 2. Instale o poetry

```
pipx install poetry
```

#### 3. Instale as dependências com Poetry:

```
cd lacrei-saude-backend

poetry install
```
#### 4. Há uma chance do Poetry não instalar algumas depdendência, execute os seguintes comandos por precaução:

```
pip install pytest

pip install sqlalchemy

pip install httpx

pip install fastapi
```

#### 5. Execute o poetry

```
poetry shell
```

#### 6. Execute a FastAPI

```
uvicorn lacrei_saude_backend.main:app --reload
```

#### 7. Acesse a interface da FastAPI

```
Digite o link http://127.0.0.1:8000/docs em seu navegador
```

## Execução de teste unitário

#### 1. Entre na pasta de testes

```
cd D:\lacrei-saude-backend\lacrei-saude-backend\tests
```

#### 2. Execute o comando

```
pytest test_api.py
```
