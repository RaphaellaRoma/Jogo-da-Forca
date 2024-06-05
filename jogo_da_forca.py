import tkinter as tk
from tkinter import ttk
import prompt

# Desenhos do boneco em ASCII
desenhos = [
    '''
     -----
     |   |
         |
         |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    '''
]

def exibir_estado_atual(palavra_secreta, letras_corretas):
    estado_atual = ''
    for letra in palavra_secreta:
        if letra in letras_corretas:
            estado_atual += letra
        else:
            estado_atual += '_'
    return estado_atual

def atualizar_jogo():
    estado_atual = exibir_estado_atual(palavra_secreta, letras_corretas)
    palavra_label.config(text="Palavra: " + estado_atual)
    letras_erradas_label.config(text="Letras erradas: " + ' '.join(letras_erradas))
    tentativas_label.config(text="Tentativas restantes: " + str(tentativas))
    desenho_label.config(text=desenhos[6 - tentativas])
    
    if estado_atual == palavra_secreta:
        resultado_label.config(text="Parabéns! Você adivinhou a palavra secreta! ◕‿◕")
        entrada.config(state=tk.DISABLED)
        botao_verificar.pack_forget()
        botao_reiniciar.pack()
        return
    
    if tentativas == 0:
        resultado_label.config(text="Você perdeu! A palavra secreta era '{}' ¯\\_(ツ)_/¯".format(palavra_secreta))
        entrada.config(state=tk.DISABLED)
        botao_verificar.pack_forget()
        botao_reiniciar.pack()

def verificar_chute(event=None):
    global tentativas
    chute = entrada.get().lower()
    entrada.delete(0, tk.END)
    
    if len(chute) == 1 and chute.isalpha():
        if chute in letras_corretas or chute in letras_erradas:
            resultado_label.config(text="Você já chutou essa letra! Tu ta realmente tentando? ( ͠° ͟ʖ ͡°)")
            return
        
        if chute in palavra_secreta:
            letras_corretas.append(chute)
        else:
            letras_erradas.append(chute)
            tentativas -= 1
    elif len(chute) == len(palavra_secreta):
        if chute == palavra_secreta:
            letras_corretas.extend(list(palavra_secreta))
        else:
            tentativas = 0
    else:
        resultado_label.config(text="sei la o que voce escreveu, digite ou uma letra ou uma palavra valida! ╰（‵□′）╯")
        return
    
    atualizar_jogo()

def reiniciar_jogo():
    global palavra_secreta, letras_corretas, letras_erradas, tentativas
    palavra_secreta = prompt.gerar_palavra(idioma, dificuldade)
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    entrada.config(state=tk.NORMAL)
    resultado_label.config(text="")
    quantidade_letras_label.config(text="A palavra secreta tem {} letras.".format(len(palavra_secreta)))
    botao_reiniciar.pack_forget()
    botao_verificar.pack()
    atualizar_jogo()

def iniciar_jogo():
    global idioma, dificuldade
    idioma = idioma_var.get()
    dificuldade = dificuldade_var.get()
    
    quantidade_letras_label.pack()
    palavra_label.pack()
    letras_erradas_label.pack()
    tentativas_label.pack()
    desenho_label.pack()
    entrada.pack()
    resultado_label.pack()
    botao_verificar.pack()

    reiniciar_jogo()
    
    idioma_label.pack_forget()
    idioma_menu.pack_forget()
    dificuldade_label.pack_forget()
    dificuldade_menu.pack_forget()
    botao_iniciar.pack_forget()

# Inicialização do jogo
idioma = ""
dificuldade = ""

letras_corretas = []
letras_erradas = []
tentativas = 6

# Interface gráfica com tkinter
root = tk.Tk()
root.title("Jogo da Forca")

# Escolha de Idioma e Dificuldade
idioma_var = tk.StringVar()
dificuldade_var = tk.StringVar()

idioma_label = tk.Label(root, text="Escolha o idioma:", font=('Helvetica', 14))
idioma_label.pack()
idioma_menu = ttk.Combobox(root, textvariable=idioma_var, font=('Helvetica', 14))
idioma_menu['values'] = ("português", "inglês", "espanhol")
idioma_menu.pack()

dificuldade_label = tk.Label(root, text="Escolha a dificuldade:", font=('Helvetica', 14))
dificuldade_label.pack()
dificuldade_menu = ttk.Combobox(root, textvariable=dificuldade_var, font=('Helvetica', 14))
dificuldade_menu['values'] = ("fácil", "médio", "difícil")
dificuldade_menu.pack()

botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo, font=('Helvetica', 14))
botao_iniciar.pack()

quantidade_letras_label = tk.Label(root, text="", font=('Helvetica', 16))
palavra_label = tk.Label(root, text="", font=('Helvetica', 16))
letras_erradas_label = tk.Label(root, text="", font=('Helvetica', 14))
tentativas_label = tk.Label(root, text="", font=('Helvetica', 14))
desenho_label = tk.Label(root, text="", font=('Courier', 14))
entrada = tk.Entry(root, font=('Helvetica', 14))
entrada.bind('<Return>', verificar_chute)
resultado_label = tk.Label(root, text="", font=('Helvetica', 14))

botao_verificar = tk.Button(root, text="Chutar", command=verificar_chute, font=('Helvetica', 14))
botao_reiniciar = tk.Button(root, text="Jogar novamente", command=reiniciar_jogo, font=('Helvetica', 14))

root.mainloop()

