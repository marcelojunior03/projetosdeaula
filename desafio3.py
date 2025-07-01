import tkinter as tk
from tkinter import messagebox

def calculo():
    nome = entrada_nome.get()
    media_exe = float(entrada_exercicios.get())
    desafio_1 = float(entrada_desafio1.get())
    desafio_2 = float(entrada_desafio2.get())
    desafio_3 = float(entrada_desafio3.get())
    fase_1 = float(entrada_fase1.get())
    fase_2 = float(entrada_fase2.get())
    fase_3 = float(entrada_fase3.get())

    media_desafios = (desafio_1 + desafio_2 + desafio_3)/3
    media_projeto = (fase_1 + fase_2 + fase_3)/3

    nota_final = (media_exe + media_desafios + (media_projeto*2))/4

    if nota_final >= 6:
        mensagem = (f"Parabéns, {nome}! Você foi aprovado com nota {nota_final}!")
        messagebox.showinfo("Resultado", mensagem)
    elif nota_final >= 4 and nota_final < 6:
        mensagem = (f"Você ainda não foi aprovado, {nome}! Sua nota foi {nota_final}. Você terá a opção de fazer o IFA!!!")
        messagebox.showinfo("Resultado", mensagem)
    elif nota_final < 4:
        mensagem = (f"Com a nota {nota_final} você não foi aprovado, {nome}! Veja pelo lado bom, você irá cursar a disciplina novamente semestre que vem!!!")
        messagebox.showinfo("Resultado", mensagem)

janela = tk.Tk()
janela.title("Calculadora de média")
janela.geometry("800x800")

rotulo_nome = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
entrada_nome = tk.Entry(janela, width=30, font=("Arial", 12))

rotulo_exercicios = tk.Label(janela, text="Insira a média dos exercícios:", font=("Arial", 12))
entrada_exercicios = tk.Entry(janela, width=5, font=("Arial", 12))

rotulo_desafio1 = tk.Label(janela, text="Insira a nota do desafio 1:", font=("Arial", 12))
entrada_desafio1 = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_desafio2 = tk.Label(janela, text="Insira a nota do desafio 2:", font=("Arial", 12))
entrada_desafio2 = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_desafio3 = tk.Label(janela, text="Insira a nota do desafio 3:", font=("Arial", 12))
entrada_desafio3 = tk.Entry(janela, width=5, font=("Arial", 12))

rotulo_fase1 = tk.Label(janela, text="Insira a nota da fase 1 do projeto:", font=("Arial", 12))
entrada_fase1 = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_fase2 = tk.Label(janela, text="Insira a nota da fase 2 do projeto:", font=("Arial", 12))
entrada_fase2 = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_fase3 = tk.Label(janela, text="Insira a nota da fase 3 do projeto:", font=("Arial", 12))
entrada_fase3 = tk.Entry(janela, width=5, font=("Arial", 12))

bt = tk.Button(janela, text="Calcular", command=calculo, font=("Arial", 10))

rotulo_nome.pack(pady=10)
entrada_nome.pack(pady=5)
rotulo_exercicios.pack(pady=10)
entrada_exercicios.pack(pady=5)
rotulo_desafio1.pack(pady=10)
entrada_desafio1.pack(pady=5)
rotulo_desafio2.pack(pady=10)
entrada_desafio2.pack(pady=5)
rotulo_desafio3.pack(pady=10)
entrada_desafio3.pack(pady=5)
rotulo_fase1.pack(pady=10)
entrada_fase1.pack(pady=5)
rotulo_fase2.pack(pady=10)
entrada_fase2.pack(pady=5)
rotulo_fase3.pack(pady=10)
entrada_fase3.pack(pady=5)
bt.pack(pady=10)

janela.mainloop()