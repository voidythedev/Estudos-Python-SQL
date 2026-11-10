import sqlite3 
import tkinter as tk

conexao = sqlite3.connect('banco_loja.db')
cursor = conexao.cursor() #Cursor é o Menssageiro

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
""")
## Cadastro manual de produtos
def cadastrar_produto():
    nome_produtos = str(input("Digite o nome do produto: "))
    estoque_produtos = int(input("Digite a quantidade em estoque: "))
    preco_produtos = float(input("Digite o preço do produto: "))

    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome_produtos, preco_produtos, estoque_produtos))
    print(f"""Produto {nome_produtos} cadastrado com sucesso!""")
conexao.commit()


def listar_produtos():
    cursor.execute("""SELECT nome, preco, estoque FROM produtos""")
    produtos = cursor.fetchall()
    
    for produto in produtos:
        nome, preco, estoque = produto
        print(f"""Nome: {nome}
Valor: {preco}              
Estoque: {estoque}""")              
        print("\n")
conexao.commit()
        
cadastrar_produto()
listar_produtos()

        
conexao.commit()

