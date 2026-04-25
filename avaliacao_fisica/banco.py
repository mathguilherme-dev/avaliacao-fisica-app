import sqlite3

DB = 'avaliacao.db'

def conectar():
    return sqlite3.connect(DB)


def criar_tabelas():
    con = conectar()
    con.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            sexo TEXT,
            peso REAL,
            altura REAL
        )
    ''')
    con.commit()
    con.close()

