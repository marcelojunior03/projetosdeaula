nome = input("Olá, qual o seu nome? ")
genero = input(f"Certo, {nome}. Agora me diga seu gênero musical favorito: ")

if genero == "pop":
    print(f"Que legal, {nome}! O meu favorito também é {genero}!")
elif genero == "rock":
    print(f"UAU! {nome}, você parece uma pessoa elétrica!")
elif genero == "sertanejo":
    print(f"Uhu! Também sou fã de uma sofrência, {nome}!")
else:
    print(f"Que interessante, {nome}. Vou tentar ficar mais por dentro desse gênero!")