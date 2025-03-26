import tkinter as tk
import random

def mover_nao(e):
    botao_nao.place(x=random.randint(50, 1000), y=random.randint(50, 700))

def resposta_sim():
    label.config(text="Sabia que você diria isso!", font=("Arial", 28))
    botao_sim.pack_forget()
    botao_nao.pack_forget()

janela = tk.Tk()
janela.title("Pergunta Importante")
janela.geometry("1280x720")

tk.Label(janela, text="Aumenta meu salário chefia?", font=("Arial", 30)).pack(pady=20)
label = tk.Label(janela, text="")
label.pack()

botao_sim = tk.Button(janela, text="Claro que sim, você merece!", font=("Arial", 18), command=resposta_sim)
botao_sim.place(x=200, y=150)

botao_nao = tk.Button(janela, text="Não, estamos em crise", font=("Arial", 18))
botao_nao.place(x=800, y=150)
botao_nao.bind("<Enter>", mover_nao)

janela.mainloop()