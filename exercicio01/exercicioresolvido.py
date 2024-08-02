# 1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: ""Telefonou para a vítima?"" ""Esteve no local do crime?"" ""Mora perto da vítima?"" ""Devia para a vítima?"" ""Já trabalhou com a vítima?"" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário,ele será classificado como""Inocente"".
# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Lista para armazenar as respostas
respostas = []

# Fazendo as perguntas
for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    respostas.append(resposta)

# Contando respostas positivas
respostas_positivas = respostas.count("sim")

# Classificação
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibindo a classificação
print("\nClassificação: " + classificacao)
