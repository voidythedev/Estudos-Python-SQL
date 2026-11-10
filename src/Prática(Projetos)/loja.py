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
    print(f"""Produto {nome_produtos} cadastrado com sucesso!""")

    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome_produtos, preco_produtos, estoque_produtos))
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
       
def atualizar_produtos():
    id_produto = int(input("Qual o ID do produto que deseja atualizar: "))
    novo_preco = float(input("Digite o novo preço do produto: "))
    novo_estoque = int(input("Digite a nova quantidade em estoque: "))

    cursor.execute("UPDATE produtos SET preco = ?, estoque = ? WHERE id = ?", (novo_preco, novo_estoque, id_produto))
    print(f"Produto {id_produto} atualizado com sucesso!")      
    conexao.commit()
    
def deletar_produto():
    id_produto = int(input("Qual o ID do produto que deseja deletar: "))
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    print(f"O produto {id_produto} foi deletado com sucesso!")
    conexao.commit()    

#cadastrar_produto()
#listar_produtos()
#atualizar_produtos()
#deletar_produto()

     
#Criação de janelas
janela = tk.Tk()
janela.title("Loja")
janela.geometry("300x400")#tamanho inicial da janela  
    
    
tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto).pack()
tk.Button(janela, text="Listar Produtos", command=listar_produtos).pack()
tk.Button(janela, text="Atualizar Produtos", command=atualizar_produtos).pack()
tk.Button(janela, text="Deletar Produto", command=deletar_produto).pack()
     
     
        
janela.mainloop()
conexao.commit()
