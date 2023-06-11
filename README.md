<div align="center">
<img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.png" style="
width: 250px;">

# API RESTful With Flask

#### API Restful feita com Python, Flask e MYSQL.
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

- Git: [Download](https://git-scm.com/downloads)
- Python 3.6+ : [Download](https://www.python.org/downloads/)
- Postman (ou um software similar): [Download](https://www.postman.com/downloads/)
- Visual Studio Code (ou um editor de código similar): [Download](https://code.visualstudio.com/download)
- MySQL Workbench v8.0+ : [Download](https://dev.mysql.com/downloads/workbench/)

---
#### 2. Criando o Banco de Dados:

Após instalar e configurar o MySQL Workbench, crie um servidor clicando no botão "+" ao lado de "MySQL Connections" na tela inicial. 
Preencha o campo "Connection Name" e clique em "Ok".

Em seguida, selecione o servidor que você criou e, na barra superior de ícones, clique em "Create new schema in connection server" para criar um schema no banco de dados.

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

---
#### 6. Conecte o banco de dados ao software

Acesse o arquivo "main.py" dentro da pasta "src"
E substitua todos as linhas os.getenv("") para os dados necessários para estabelecer a conexão, ficando assim aproxidamente:

```connection = pymysql.connect(
    host = root,
    user = "meuNomeDeUsuário",
    password = "minhaSenha",
    database = "nomeDoMeuSchema",
    )
```

certifique de todos os dados substituidos estarem certos e entre aspas.

---
#### 7. Execute o arquivo main.py

Basta clicar F8 em seu teclado ou clicar no botão de "play" no canto superior direito caso esteja no Visual Studio Code.

Se tudo estiver correto, sua API estára no ar e basta testar usando o POSTMAN ou Serviços similares.

OBS: Configure o header como:
"Content-Type", 'application/json" dentro do Postman.