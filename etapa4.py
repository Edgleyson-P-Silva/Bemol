import requests

# Configurações básicas
BASE_URL = "https://serverest.dev"
HEADERS = {"Content-Type": "application/json"}

# Dados para os testes
usuario = {
    "nome": "Edgleyson Silva",
    "email": "edgleysonsilva99@gmail.com",
    "password": "qaenginnerbemol2024",
    "administrador": "true"
}

produto = {
    "nome": "Produto Bemol",
    "preco": 100,
    "descricao": "Lojas Bemol",
    "quantidade": 100
}

def criar_usuario():
    """Cria um novo usuário e retorna o ID do usuário criado."""
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario, headers=HEADERS)
    print(f"Create User Response: {response.status_code}, {response.text}")
    if response.status_code == 201:
        return response.json().get('id')
    else:
        raise Exception("Erro ao criar o usuário.")

def verificar_usuario(usuario_id):
    """Verifica se o usuário foi criado com o ID fornecido."""
    response = requests.get(f"{BASE_URL}/usuarios/{usuario_id}", headers=HEADERS)
    print(f"Verify User Response: {response.status_code}, {response.text}")
    if response.status_code == 200:
        user_data = response.json()
        assert user_data['nome'] == usuario['nome'], "Nome do usuário não corresponde."
        assert user_data['email'] == usuario['email'], "Email do usuário não corresponde."
    else:
        raise Exception("Erro ao buscar o usuário.")

def criar_produto():
    """Cria um novo produto e retorna o ID do produto criado."""
    response = requests.post(f"{BASE_URL}/produtos", json=produto, headers=HEADERS)
    print(f"Create Product Response: {response.status_code}, {response.text}")
    if response.status_code == 201:
        return response.json().get('id')
    else:
        raise Exception("Erro ao criar o produto.")

def verificar_produto(produto_id):
    """Verifica se o produto foi criado com o ID fornecido."""
    response = requests.get(f"{BASE_URL}/produtos/{produto_id}", headers=HEADERS)
    print(f"Verify Product Response: {response.status_code}, {response.text}")
    if response.status_code == 200:
        product_data = response.json()
        assert product_data['nome'] == produto['nome'], "Nome do produto não corresponde."
        assert product_data['preco'] == produto['preco'], "Preço do produto não corresponde."
    else:
        raise Exception("Erro ao buscar o produto.")

def main():
    try:
        # Teste para criação e verificação de usuário
        usuario_id = criar_usuario()
        verificar_usuario(usuario_id)

        # Teste para criação e verificação de produto
        produto_id = criar_produto()
        verificar_produto(produto_id)

        print("Todos os testes foram realizados com sucesso!")

    except Exception as e:
        print(f"Erro durante os testes: {e}")

if __name__ == "__main__":
    main()
