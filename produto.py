nome_produto = input("digite o nome do produto: ")
preço = float(input("digite o preço do produto: "))
desconto = float(input("digite o percentual de desconto: "))
valor_desconto = preço * desconto/100
preco_final = preço - valor_desconto
print(f"produto: {nome_produto} - preço final: R$ {preco_final}")