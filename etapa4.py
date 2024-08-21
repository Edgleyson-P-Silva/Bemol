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