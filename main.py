import json
import os

# Caminho do arquivo JSON
file_path = 'inventario.json'

# Função para carregar os produtos
def carregar_inventario():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Função para salvar os produtos no arquivo JSON
def salvar_inventario(inventario):
    with open(file_path, 'w') as file:
        json.dump(inventario, file, indent=2)

# Função para garantir que a entrada de um número seja válida
def ler_numero(prompt, tipo=float):
    while True:
        try:
            valor = tipo(input(prompt))
            return valor
        except ValueError:
            print(f"Valor inválido! Por favor, insira um número válido.")

# Função para adicionar um novo produto
def adicionar_produto(inventario):
    nome = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    quantidade = ler_numero("Quantidade em Estoque: ", int)
    preco = ler_numero("Preço: ")

    # Gerar um ID único (simplesmente baseado no comprimento da lista)
    id_produto = len(inventario) + 1
    produto = {
        'id': id_produto,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco
    }

    inventario.append(produto)
    salvar_inventario(inventario)
    print(f'Produto "{nome}" adicionado com sucesso!')

# Função para listar todos os produtos com ordenação
def listar_produtos(inventario):
    if len(inventario) == 0:
        print("Nenhum produto encontrado.")
    else:
        criterio = input("Escolha um critério para ordenação (nome, preco, quantidade): ").lower()
        if criterio not in ['nome', 'preco', 'quantidade']:
            print("Critério inválido! Usando 'nome' por padrão.")
            criterio = 'nome'

        inventario_ordenado = sorted(inventario, key=lambda x: x[criterio])
        
        print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Qtd':<10} {'Preço':<10}")
        print("-" * 60)
        for produto in inventario_ordenado:
            print(f"{produto['id']:<5} {produto['nome']:<20} {produto['categoria']:<15} {produto['quantidade']:<10} {produto['preco']:<10.2f}")

# Função para atualizar um produto
def atualizar_produto(inventario):
    id_produto = ler_numero("Informe o ID do produto a ser atualizado: ", int)
    produto = next((p for p in inventario if p['id'] == id_produto), None)

    if produto:
        print(f"Produto encontrado: {produto['nome']}")
        nome = input(f"Novo nome (atual: {produto['nome']}): ")
        categoria = input(f"Nova categoria (atual: {produto['categoria']}): ")
        quantidade = input(f"Nova quantidade (atual: {produto['quantidade']}): ")
        preco = input(f"Novo preço (atual: {produto['preco']}): ")

        produto['nome'] = nome or produto['nome']
        produto['categoria'] = categoria or produto['categoria']
        produto['quantidade'] = int(quantidade) if quantidade else produto['quantidade']
        produto['preco'] = float(preco) if preco else produto['preco']

        salvar_inventario(inventario)
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado!")

# Função para excluir um produto
def excluir_produto(inventario):
    id_produto = ler_numero("Informe o ID do produto a ser excluído: ", int)
    produto = next((p for p in inventario if p['id'] == id_produto), None)

    if produto:
        confirmacao = input(f"Tem certeza que deseja excluir o produto {produto['nome']}? (s/n): ")
        if confirmacao.lower() == 's':
            inventario.remove(produto)
            salvar_inventario(inventario)
            print(f"Produto {produto['nome']} excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Produto não encontrado!")

# Função para buscar um produto
def buscar_produto(inventario):
    termo = input("Buscar por ID ou Nome: ").lower()
    resultados = [p for p in inventario if str(p['id']) == termo or termo in p['nome'].lower()]

    if resultados:
        for produto in resultados:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")
    else:
        print("Nenhum produto encontrado.")

# Menu principal
def menu():
    inventario = carregar_inventario()

    while True:
        print("\nGerenciamento de Produtos - AgilStore")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto(inventario)
        elif opcao == '2':
            listar_produtos(inventario)
        elif opcao == '3':
            atualizar_produto(inventario)
        elif opcao == '4':
            excluir_produto(inventario)
        elif opcao == '5':
            buscar_produto(inventario)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
