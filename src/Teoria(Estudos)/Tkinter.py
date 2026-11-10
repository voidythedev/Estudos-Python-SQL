import tkinter as tk

janela = tk.Tk()
janela.title("Teste TK")
janela.geometry("400x300")#tamanho inicial da janela

#tk.Label(janela, text=(f"{nome}")).pack()#Label é um rótulo, uma caixa de texto



texto = tk.Label(janela, text="Bem, vindo(a)!")#Label é um rótulo, uma caixa de texto
texto.pack()

def resposta_botao():
    nome = entrada_texto.get()#Pega o texto digitado na Entry
    texto["text"] = f"Olá, {nome}! Prazer em te conhecer !"#Alterando o texto do Label
    

entrada_texto = tk.Entry(janela)
entrada_texto.pack()#Entry é uma caixa de entrada de texto

tk.Button(janela, text="Apresentar-se", command=resposta_botao).pack()#Button é um botão, command é o comando que será executado ao clicar no botão

janela.mainloop()