import requests
from PIL import Image, ImageTk
import tkinter as tk
import random
import io

# Lista de URLs de imagens do Nicolas Cage
imagens_nicolas_cage = [
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/1.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/2.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/3.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/4.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/5.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/6.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/7.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/8.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/9.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/10.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/11.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/12.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/13.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/14.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/15.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/16.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/17.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/18.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/19.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/20.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/21.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/22.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/23.jpg",
    "https://startie.com.br/projetos-meme/projeto-nicolas-cage/imgs/24.jpg",
]

# Tempo em milissegundos entre as janelas
TEMPO_JANELA_MS = 2000  # 2 segundos

# Função para abrir uma nova janela com a imagem
def abrir_janela(imagem_url, x, y):
    # Cria uma nova janela
    janela = tk.Toplevel()
    janela.geometry(f"720x720+{x}+{y}")
    
    # Busca a imagem
    resposta = requests.get(imagem_url)
    
    # Verifica se a resposta é uma imagem
    if resposta.status_code == 200 and 'image' in resposta.headers['Content-Type']:
        try:
            imagem = Image.open(io.BytesIO(resposta.content))
            # Converte a imagem para um formato que o tkinter pode usar
            imagem_tk = ImageTk.PhotoImage(imagem)
            
            # Cria um rótulo para exibir a imagem
            rotulo = tk.Label(janela, image=imagem_tk)
            rotulo.image = imagem_tk  # Mantém uma referência da imagem
            rotulo.pack()
        except Exception as e:
            print(f"Erro ao abrir a imagem: {e}")
    else:
        print(f"Erro ao carregar a imagem: {imagem_url}")

# Função para abrir janelas em intervalos
def abrir_janelas_com_intervalo(index=0):
    imagem_url = imagens_nicolas_cage[index]
    x = random.randint(0, 1920)  # Posição aleatória na tela
    y = random.randint(0, 1080)
    abrir_janela(imagem_url, x, y)
    
    # Incrementa o índice para a próxima imagem (ciclo infinito)
    index = (index + 1) % len(imagens_nicolas_cage)  # Reinicia no início quando chega ao fim
    root.after(TEMPO_JANELA_MS, abrir_janelas_com_intervalo, index)  # Chama a próxima abertura

# Configuração da janela principal
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    abrir_janelas_com_intervalo()  # Inicia a lógica de abertura das janelas
    root.mainloop()
