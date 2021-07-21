from tkinter import *
import random

janela = Tk()
janela.title("GERADOR DE SENHAS")
altura = 500
largura = 500
janela.resizable(True, True)
janela.configure(bg='white')
alturatela = janela.winfo_screenheight()
larguratela = janela.winfo_screenwidth()
posx = larguratela/2 - largura/2
posy = alturatela/2  - altura/2
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.columnconfigure(0,weight=1)

def gerarSenha():
    usuario = loginVar.get()
    servico = redeSocialVar.get()
    quantidadeChar = senhaCaracter.get()
    listaDeChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890/*-+.<>:/?]}[{=+_()&%$#@!'
    caracteres = random.choices(listaDeChar,k=(int(quantidadeChar)))
    nova_senha = ''.join(caracteres)
    registrar_senha(nova_senha, servico, usuario)

def registrar_senha(nova_senha, servico, usuario):
    with open('Gerador de Senhas.txt','a',newline='') as arquivo:
        arquivo.write(f"\n*****" + servico.upper() + "***** \n" + "Usuario: " + usuario + "\n" + "Senha: " + nova_senha + "\n" + "*****************" + "\n")

    mensagemFinal = Label(janela,text="\n O arquivo foi salvo! \n", bg='white')
    mensagemFinal.grid(column=0, row=9)

img = PhotoImage(file="Imagem/download.png")
label_imagem = Label(janela,image=img, bg='white')

texto_apresentacao = Label(janela, text=" \n \n BEM VINDO AO GERENCIADOR DE SENHAS \n", bg='white')

texto_orientacao = Label(janela, text="FAVOR PREENCHER TODOS OS DADOS\n", bg='white')

texot_pergunta1 = Label(janela, text="Para qual REDE SOCIAL ou SERVIÇO se destina essa senha ? ", bg='white')

redeSocialVar = StringVar
redeSocialVar =  Entry(janela, width=50, textvariable = redeSocialVar)

texot_pergunta2 = Label(janela, text="\n Qual é o E-MAIL ou nome de USUARIO para qual se destina essa senha ?  ", bg='white')

loginVar = StringVar
loginVar =  Entry(janela, width=50, textvariable = loginVar)

texot_pergunta3 = Label(janela, text="\n Qual é a QUANTIDADE de caracteres ? ", bg='white')

senhaCaracter = StringVar
senhaCaracter =  Entry(janela, width=50, textvariable = senhaCaracter)

botao = Button(janela,text="Gerar senhas", command=gerarSenha)

label_imagem.grid(column=0, row=0)
texto_apresentacao.grid(column=0, row=1)
texto_orientacao.grid(column=0, row=2)
texot_pergunta1.grid(column=0, row=3)
redeSocialVar.grid(column=0, row=4)
texot_pergunta2.grid(column=0, row=5)
loginVar.grid(column=0, row=6)
texot_pergunta3.grid(column=0, row=7)
senhaCaracter.grid(column=0, row=8)
botao.grid(column=0,row=9)
janela.mainloop()

