import requests #requisicoes http para ineragir com a api

url_base = "https://serverest.dev"
headers = HEADERS = {"Content-Type": "application/json"}  # Cabeçalhos HTTP em json

usuario = {
    "nome": "Edgleyson Silva",  # Nome do usuário a ser criado
    "email": "edgleyson99@outlook.com",  # Email do usuário a ser criado
    "password": "qaenginnerbemol2024",  # Senha do usuário a ser criada
    "administrador": "true"  # Define se o usuário é um administrador
}

produto = {
    "nome": "Produto Bemol",  # Nome do produto a ser criado
    "preco": 100,  # Preço do produto
    "descricao": "Lojas Bemol",  # Descrição do produto
    "quantidade": 100  # Quantidade do produto em estoque
}

def criar_usuario():

    # Envia uma requisição para criar um novo usuário na API
    response = requests.post(f"{url_base}/usuarios", json=usuario, headers=HEADERS)
    
    # Imprime o status e o corpo da resposta
    print(f"Resposta do usuário criado: {response.status_code}, {response.text}")
    
    # Verifica se a requisição foi bem-sucedida (código 201 na API)
    if response.status_code == 201:
        # Retorna o ID do usuário criado a partir da resposta JSON
        return response.json().get('id')
    else:
        # Levanta uma exceção se a requisição falhar, com uma mensagem de erro
        raise Exception("Erro ao criar o usuário.")
    
def verificar_usuario(usuario_id):

    # Buscar o usuário pelo ID na API
    response = requests.get(f"{url_base}/usuarios/{usuario_id}", headers=HEADERS)
    
    # Imprime o status
    print(f"Verificar resposta do usuário: {response.status_code}, {response.text}")
    
    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Obtém os dados do usuário da resposta JSON
        user_data = response.json()
        
        # Verificar se o nome retornado corresponde ao nome esperado
        assert user_data['nome'] == usuario['nome'], "Nome do usuário não corresponde."
        
        # Verificar se o email retornado corresponde ao email esperado
        assert user_data['email'] == usuario['email'], "Email do usuário não corresponde."
    else:
        # Levanta uma exceção se a requisição falhar, com uma mensagem de erro
        raise Exception("Erro ao buscar o usuário.")
    
def criar_produto():

    # Criar um novo produto na API
    response = requests.post(f"{url_base}/produtos", json=produto, headers=HEADERS)
    
    # Imprime o status
    print(f"Criar produto: {response.status_code}, {response.text}")
    
    # Verifica se foi bem-sucedida (código 201 Created)
    if response.status_code == 201:
        # Retorna o ID do produto criado a partir da resposta
        return response.json().get('id')
    else:
        # Levanta uma exceção se a requisição falhar, com uma mensagem
        raise Exception("Erro ao criar o produto.")

def verificar_produto(produto_id):

    # buscar o produto pelo ID na API
    response = requests.get(f"{url_base}/produtos/{produto_id}", headers=HEADERS)
    
    print(f"Verify Product Response: {response.status_code}, {response.text}")
    
    # (código 200 OK)
    if response.status_code == 200:
        # Dsdos do produto da resposta JSON
        product_data = response.json()
        
        # Verifica o nome
        assert product_data['nome'] == produto['nome'], "Nome do produto não corresponde."
        
        # Verifica preço
        assert product_data['preco'] == produto['preco'], "Preço do produto não corresponde."
    else:
        # Se falahr mensagem de erro
        raise Exception("Erro ao buscar o produto.")
    
    
    
# Testa a criação e verificação de um usuário
usuario_id = criar_usuario()  # Cria um novo usuário e obtém o ID
verificar_usuario(usuario_id)  # Verifica se o usuário foi criado corretamente

# Testa a criação e verificação de um produto
produto_id = criar_produto()  # Cria um novo produto e obtém o ID
verificar_produto(produto_id)  # Verifica se o produto foi criado corretamente

# Mensagem de sucesso se todos os testes passarem
print("Todos os testes foram realizados com sucesso!")
