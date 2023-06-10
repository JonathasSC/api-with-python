# api-with-python
Create API REST with Python Flask

### Como usar?

<div align="center">
<img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.png" style="
width: 250px;">

# Api With Flask

#### Projeto feito em Python Flask
</div>

---
### Tecnologias utilizadas

![python](https://img.shields.io/badge/PYTHON-306998?&logo=python&logoColor=ffdd54&style=flat&logoWidth=30) ![mysql](https://img.shields.io/badge/MYSQL-1E4C68?&logo=mysql&logoColor=white&style=flat&logoWidth=30) ![flask](https://img.shields.io/badge/FLASK-black?&logo=flask&logoColor=white&style=flat&logoWidth=30)

### Ferramentas utilizadas

![vscode](https://img.shields.io/badge/VS%20CODE-0078d7?&logo=visualstudiocode&logoColor=white&style=flat&logoWidth=30) ![mysql](https://img.shields.io/badge/MYSQL_WORKBENCH-1E4C68?&logo=mysql&logoColor=white&style=flat&logoWidth=30) ![postman](https://img.shields.io/badge/POSTMAN-orange?&logo=postman&logoColor=white&style=flat&logoWidth=30)

---

<div align="center">

## Como utilizar?
</div>

### 1. Tenha os itens e ambientes necessários

#### 1.1 Linguagens e Aplicações:
###### 1.1.1 Git
Link de download:
https://git-scm.com/downloads
###### 1.1.2 Python v3.6+
Download:
https://www.python.org/downloads/
###### 1.1.3 Postman (ou similar)
Link de download:
https://www.postman.com/downloads/

###### 1.1.4 Visual Studio Code (ou similar)
Link de download:
https://code.visualstudio.com/download

#### 1.2 Banco de dados:
###### 1.2.1 MySQL workbench v8.0+
Link de download:
https://dev.mysql.com/downloads/workbench/

---
#### 2. Criando o Banco de Dados:

Após instalar e configurar inicialmente o MySQL Workbench, na tela inicial será necessário criar um servidor, no botão "+" ao lado de MySQL connections

Preencha o campo "Connection Name" e clique em "Ok" e clique nesse servidor criado.

Após isso, perceba uma barra superior com icones e clique em "Create new schema in connection server." para criar um schema

E finalize a criação do schema.

---
#### 3. Clone esse repositório e acesse:

Dentro de uma pasta, abra um terminal ou bash, e digite:

``` git clone https://github.com/JonathasSC/api-with-python.git ```

depois

``` cd api-with-python ```

---
#### 4. Crie um ambiente virtual e instale os pacotes necessários:

Ainda com o terminal ou bash, execute essa sequencia:

``` python -m venv venv ```

``` venv/Scripts/Activate ```

``` pip install -r requirements.txt ``` 

---
#### 5. Abra o repositorio em um editor de código.

Caso você esteja utilizando o visual studio code, ainda no terminal/bash você pode dar o seguinte comando:

``` code .```

Isso abrirá o repositorio automaticamente dentro do Visual Studio Code 

Caso esteja usando outro editor, basta importar o diretorio/repositorio local para dentro do editor.

#### 6. Conecte o banco de dados ao software

Acesse o arquivo "main.py" dentro da pasta "src"
E substitua todos as linhas os.getenv("") para os dados necessários para estabelecer a conexão, ficando assim aproxidamente:

connection = pymysql.connect(
    host = root,
    user = "meuNomeDeUsuário",
    password = "minhaSenha",
    database = "nomeDoMeuSchema",
    )

certifique de todos os dados substituidos estarem certos e entre aspas.

#### 7. Execute o arquivo main.py

Basta clicar F8 em seu teclado ou clicar no botão de "play" no canto superior direito caso esteja no Visual Studio Code.

Se tudo estiver correto, sua API estára no ar e basta testar usando o POSTMAN ou Serviços similares.

OBS: Configure o header como:
"Content-Type", 'application/json" dentro do Postman.