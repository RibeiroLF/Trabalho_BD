# Trabalho_BD
## Sistema de controle do RU

### Introdução
O sistema de controle do Restaurante Universtário (RU) tem o objetivo de armazenar e fornecer informações sobre o menu semanal, incluindo suas refeições (café da manhã, almoço e jantar), pratos, bebidas e complementos. 

### Links
#### Modelo de Entidade Relacionamento
[https://app.brmodeloweb.com/#!/publicview/6831c9cfbab8ef5faf4645a4](https://app.brmodeloweb.com/#!/publicview/6831c9cfbab8ef5faf4645a4)
#### Modelo Relacional
[https://app.brmodeloweb.com/#!/publicview/68322134bab8ef5faf46556a](https://app.brmodeloweb.com/#!/publicview/6869358c2684859699822cbb)

---

### Como Executar o Projeto

O projeto consiste em um backend (API) feito em Python com Flask e um frontend feito em React que roda diretamente no navegador.

#### 1. Pré-requisitos
- **Python 3.8** ou superior.
- **pip** (gerenciador de pacotes do Python).

#### 2. Configuração do Banco de Dados
A aplicação requer um servidor de banco de dados MySQL.
1.  **Crie o Esquema:** Execute o script `SQL.txt` em seu servidor MySQL para criar todas as tabelas e relacionamentos necessários.
2.  **Popule o Banco:** Execute o script `SQL_dados.sql` para popular o banco de dados com os dados iniciais de exemplo.

#### 3. Configuração do Backend
O backend é responsável por se comunicar com o banco de dados e fornecer os dados para o frontend.

1.  **Crie um Ambiente Virtual (Recomendado):**
    ```bash
    # Crie uma pasta para o ambiente virtual
    python -m venv venv
    # Ative o ambiente virtual
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

2.  **Instale as Dependências:**
    Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
    ```
    Flask
    PyMySQL
    Flask-Cors
    ```
    Em seguida, instale as dependências com o pip:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure a Conexão:**
    Abra o arquivo `db.py` e certifique-se de que as credenciais de acesso (host, porta, usuário, senha e nome do banco) estão corretas.

#### 4. Executando a Aplicação
Com o backend configurado e o ambiente virtual ativado, você pode iniciar o servidor.

1.  **Inicie o Servidor Flask:**
    No terminal, na raiz do projeto, execute o comando:
    ```bash
    python app.py
    ```
    O servidor começará a rodar e exibirá mensagens no terminal, incluindo o endereço local.

2.  **Acesse a Aplicação:**
    Abra seu navegador de internet e acesse o seguinte endereço:
    ```
    [http://12.0.0.1:5000](http://12.0.0.1:5000)
    ```
    A interface do sistema de controle do RU, feita em React, será carregada, e você poderá interagir com os dados do seu banco.
