from flask import Flask, jsonify, make_response, request
import pymysql
import dotenv
import os

# ============ CARREGANDO VARIAVEIS ================================== #
dotenv.load_dotenv(dotenv.find_dotenv())

# ============ CONFIG CONEXÃO ======================================== #
pymysql.install_as_MySQLdb()

connection = pymysql.connect(
    host = os.getenv("YOUR_HOST"),
    user = os.getenv("YOUR_USER"),
    password = os.getenv("YOUR_PASSWORD"),
    database = os.getenv("YOUR_DATABASE"),
    )

cursor = connection.cursor()

# Iniciando app Flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# ============ CREATE TABLE =========================================== #
def create_table():
    cursor = connection.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS users (
    id      INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name    VARCHAR(100),
    surname VARCHAR(100),
    email   VARCHAR(100)
    );
    '''
    cursor.execute(sql)

create_table()

# ============= CRUD ================================================== #
# ------------ CREATE USER -------------------------------------------- #
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')

    sql = "INSERT INTO users (name, surname, email) VALUES (%s, %s, %s);"

    cursor.execute(sql, (name, surname, email))
    connection.commit()

    return {'message':'create success'}


# ------------ READ ALL ----------------------------------------------- #
@app.route('/users', methods=['GET'])
def get_all_users():

    sql = "SELECT * FROM users"
    cursor.execute(sql)
    rows = cursor.fetchall()

    users = []
    for row in rows:
        user = {
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "email": row[3],
        }
        users.append(user)

    return make_response(jsonify(users))


# ------------ READ USER ---------------------------------------------- #
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    sql = "SELECT * FROM users WHERE ID = %s;"
    
    cursor.execute(sql,(id,))
    rows = cursor.fetchall()
    
    for row in rows:
        user = {
            "id": row[0],
            "name": row[1],
            "surname": row[2],
            "email": row[3],
        }

    return make_response(jsonify(user))


# ------------ UPDATE ALL -------------------------------------------- #
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')

    cursor = connection.cursor()
    sql = "UPDATE users SET name = %s, surname = %s, email = %s WHERE id = %s;"
    cursor.execute(sql, (name, surname, email, id))
    connection.commit()

    updated_user = {
        "id": id,
        "name": name,
        "surname": surname,
        "email": email
    }

    return make_response(jsonify(updated_user))


# ------------ DELETE ------------------------------------------------ #
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    sql = "DELETE FROM users WHERE ID = %s;"
    
    cursor.execute(sql,(id,))
    connection.commit()

    return {'message':'delete success'}



app.run()