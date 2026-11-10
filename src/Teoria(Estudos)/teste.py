import sqlite3

conexao = sqlite3.connect('bancotestepy.db')
cursor = conexao.cursor() #Cursor é o Menssageiro 

## Criando a tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titular TEXT NOT NULL,
        saldo FLOAT NOT NULL,
        cpf TEXT NOT NULL UNIQUE
        )""")

cursor.execute ("""INSERT INTO contas_bancarias (titular, saldo, cpf) VALUES
                ('Miguel', 5600.00, '132.455.789-00')""")

cursor.execute("""SELECT * FROM contas_bancarias""")
contas = cursor.fetchall()
#cursor.execute("""DELETE FROM contas_bancarias WHERE id = 1""")
#cursor.execute("""UPDATE contas_bancarias 
#               SET saldo = 3000.00   WHERE id = 2""")


for conta in contas:
    id, titular, saldo, cpf = conta
    print(f"""Id: {id}
Titular: {titular}
Saldo: {saldo}
CPF: {cpf}""")#fetchall() retorna todos os registros da tabela
    print("\n")
conexao.commit() #Salvando as alterações
        
        
