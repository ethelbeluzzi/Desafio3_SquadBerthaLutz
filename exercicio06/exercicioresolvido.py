#recebe a entrada
nome = input("Digite seu nome: ")

#normatiza tudo em maiúscula
nome = nome.upper()

#adiciona cada uma das letras a uma string vazia no ordem inversa
inverso = ''.join(reversed(nome))
print(f'{nome} seu nome invertido fica: {inverso}')