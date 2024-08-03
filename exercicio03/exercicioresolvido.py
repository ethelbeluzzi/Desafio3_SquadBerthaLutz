# 3. Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

carrinho = {}


carrinho["arroz"] = 3
carrinho["feijao"] = 2
carrinho["laranja"] = 12
carrinho["chocolate"] = 5
carrinho["leite"] = 4


total = sum(carrinho.values())


print(f"{"Item":<15}{"Quantidade":<10}\n")

for item, quantidade in carrinho.items():
    print(f"{item:<14} {quantidade:<10}")


print(f"\nTotal de itens no carrinho: {total}")
