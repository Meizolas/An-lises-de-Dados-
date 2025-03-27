import pymysql
import pandas as pd
import sqlalchemy 

USUARIO = "seu_usuario"
SENHA = "sua_senha"
HOST = "localhost"
BANCO = "seu_banco"
ARQUIVO_CSV = "Relatorio_cadop.csv"

conn = pymysql.connect(host=HOST, user=USUARIO, password=SENHA, database=BANCO)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS relatorio_cadop (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        idade INT,
        cidade VARCHAR(100),
        data_registro DATE
    );
''')

