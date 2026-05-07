import sqlite3
from datetime import date


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
    con.execute('''
                CREATE TABLE IF NOT EXISTS avaliacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_id INTEGER,
                    data TEXT,
                    peso REAL,
                    gordura REAL,
                    massa_gorda REAL,
                    massa_magra REAL,
                    imc REAL,
                    rcq REAL,
                    soma_dobras REAL,
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
                    )
    ''')
    con.commit()
    con.close()

def salvar_aluno(nome, idade, sexo, peso, altura):
    con = conectar()
    con.execute('''
        INSERT INTO alunos (nome, idade, sexo, peso, altura)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, idade, sexo, peso, altura))
    con.commit()
    con.close()

def listar_alunos():
    con = conectar()
    alunos = con.execute('SELECT * FROM alunos').fetchall()
    con.close()
    return alunos

def buscar_aluno(aluno_id):
    con = conectar()
    aluno = con.execute('SELECT * FROM alunos WHERE id = ?',(aluno_id,)
    ).fetchone()
    con.close()
    return aluno

def excluir_aluno(aluno_id):
    con = conectar()
    con.execute(
        'DELETE FROM alunos WHERE id = ?', (aluno_id,)
    )
    con.commit()
    con.close()

def atualizar_aluno(aluno_id, nome, idade, sexo, peso, altura):
    con = conectar()
    con.execute('''
        UPDATE alunos
        SET nome = ?, idade = ?, sexo = ?, peso = ?, altura = ?
        WHERE id = ?
    ''', (nome, idade, sexo, peso, altura, aluno_id))


def salvar_avaliacao(aluno_id, soma_dobras, gordura, massa_gorda, massa_magra, imc, rcq, peso):
    con = conectar()
    con.execute('''
                INSERT INTO avaliacoes (aluno_id, data, peso, gordura, massa_gorda, massa_magra, imc, rcq, soma_dobras)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (aluno_id, str(date.today()), peso, gordura, massa_gorda, massa_magra, imc, rcq, soma_dobras))
    con.commit()
    con.close()
