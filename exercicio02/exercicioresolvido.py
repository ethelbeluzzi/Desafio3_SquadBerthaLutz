# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

numero = input("Digite um Número:")

def reverso(numero):

    numero_reverso = (numero[::-1])
    return numero_reverso

print(f"O reverso de {numero} é {reverso(numero)}.")
