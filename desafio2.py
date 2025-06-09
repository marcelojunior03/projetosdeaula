import tkinter as tk
from tkinter import messagebox

def calculo():
    valor = float(entrada_valor.get())
    idade = int(entrada_idade.get())
    clube = int(entrada_clube.get())
    niver = int(entrada_niver.get())

    if valor <= 100:
        valor = valor
    elif (clube == 1) and (niver == 1):
        valor = valor - 15
    elif (clube == 1) or (idade >= 60):
        valor = valor - 10
    else:
        valor = valor
    
    mensagem = (f"Sua compra deu um total de R${valor}.")
    rotulo_resultado.config(text=mensagem)
    messagebox.showinfo("Resultado", mensagem)

janela = tk.Tk()
janela.title("Promoção supermercado Delta")
janela.geometry("500x500")

rotulo_instrucao = tk.Label(janela, text="Olá, digite o valor da compra:", font=("Arial", 12))
entrada_valor = tk.Entry(janela, width=30, font=("Arial", 12))
rotulo_instrucao2 = tk.Label(janela, text="Insira sua idade:", font=("Arial", 12))
entrada_idade = tk.Entry(janela, width=30, font=("Arial", 12))
rotulo_instrucao3 = tk.Label(janela, text="Digite 1 se hoje for seu aniversário e 0 se não for:", font=("Arial", 12))
entrada_niver = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_instrucao4 = tk.Label(janela, text="Se você for sócio do Clube Delta, digite 1. Se não for, digite 0:", font=("Arial", 12))
entrada_clube = tk.Entry(janela, width=5, font=("Arial", 12))
bt = tk.Button(janela, text="Enviar", command=calculo, font=("Arial", 10))
rotulo_resultado = tk.Label(janela, text="", font=("Arial", 12))

rotulo_instrucao.pack(pady=10)
entrada_valor.pack(pady=5)
rotulo_instrucao2.pack(pady=10)
entrada_idade.pack(pady=5)
rotulo_instrucao3.pack(pady=10)
entrada_niver.pack(pady=5)
rotulo_instrucao4.pack(pady=10)
entrada_clube.pack(pady=5)
bt.pack(pady=10)
rotulo_resultado.pack(pady=10)

janela.mainloop()