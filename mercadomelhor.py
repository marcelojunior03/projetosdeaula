from datetime import datetime

data_hoje = datetime.today()

valor = float(input("Olá, digite o valor da compra:\nR$"))
nascimento = input("Agora, insira sua data de nascimento (no modelo dd/mm/aaaa):\n")
nascimento_dati = datetime.strptime(nascimento, "%d/%m/%Y")
idade = data_hoje.year - nascimento_dati.year
if data_hoje.month < nascimento_dati.month or (data_hoje.month == nascimento_dati.month and data_hoje.day < nascimento_dati.day):
    idade -= 1
clube = int(input("Se você for sócio do Clube Delta, digite 1. Se não for, digite 0:\n"))

if valor <= 100:
    print(f"Sua compra deu um total de R${valor}")
elif (clube == 1) and (data_hoje.month == nascimento_dati.month and data_hoje.day == nascimento_dati.day):
    print(f"Sua compra deu um total de R${valor - 15}")
elif (clube == 1) or (idade > 60):
    print(f"Sua compra deu um total de R${valor - 10}")
else:
    print(f"Sua compra deu um total de R${valor}")