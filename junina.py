rep = 1
dicio = {}

while rep == 1:
    produto = input("Qual produto deseja adicionar?\n")
    valor = float(input("Qual o valor do produto?\n"))
    dicio[f"{produto}"] = f"{valor}"
    print(dicio)
    rep = int(input("Se deseja adicionar mais produtos, degite 1. Se deseja finalizar, digite 0.\n"))

print("Lista final:\n")
print(dicio)