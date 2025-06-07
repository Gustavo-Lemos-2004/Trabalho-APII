import sqlite3
from flask import Flask

def cadastrar_admin():
    nome = str(input("Nome: "))
    cpf = int(input("CPF: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    con = sqlite3.connect("administradores.db")
    cursor = con.cursor()
    sql = "INSERT INTO administradores (nome, cnpj, email, senha) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (nome, cpf, email, senha))
    con.commit()
    with open('adms.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome}\n{cpf}\n{email}\n{senha}\n\n")
    con.close()
    

def deletar_admin():
    x = int(input("ID: "))
    con = sqlite3.connect("administradores.db")
    cursor = con.cursor()
    sql = "DELETE FROM administradores WHERE id = ? "
    cursor.execute(sql, (x,))
    todos_adms=cursor.fetchall()
    con.commit()
    con.close()
    with open("adms.txt", "w", encoding="utf-8") as arquivo:
        for nome, cpf, email, senha in todos_adms:
            arquivo.write(f"{nome} | {cpf} | {email} | {senha}\n")

def editar_admin():
    x = int(input("ID: "))
    nome = str(input("Nome: "))
    cpf = int(input("CPF: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    con = sqlite3.connect("administradores.db")
    cursor = con.cursor()
    sql = "UPDATE administradores SET nome=?, cnpj=?, email=?, senha=? WHERE id=?"
    cursor.execute(sql, (nome, cpf, email, senha, x))
    adms_atualizados = cursor.fetchall()
    conn.close()
    con.commit()
    con.close()
    with open("adms.txt", "w", encoding="utf-8") as arquivo:
        for nome, cpf, email, senha in adms_atualizados:
            arquivo.write(f"{nome}\n{cpf}\n{email}\n{senha}\n\n")


escolha = int(input("Escolha: "))
if escolha == 1:
    cadastrar_admin()
if escolha == 2:
    editar_admin()
if escolha == 3:
    deletar_admin()
