alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def troca(pl, indice):
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = i+(indice)
        while i > 25:
            i -= 26
        cripto.append(alfabeto[i])
    return cripto

palavra = input("Digite uma palavra: ")
chave = int(input("Em qual chave ela deve ser criptografada? "))

lista = troca(palavra, chave)

print(lista)
