import requests #requisicoes http para ineragir com a api

url_base = "https://serverest.dev"
headers = HEADERS = {"Content-Type": "application/json"}  # Cabeçalhos HTTP em json

usuario = {
    "nome": "Edgleyson Silva",  # Nome do usuário a ser criado
    "email": "edgleyson99@outlook.com",  # Email do usuário a ser criado
    "password": "qaenginnerbemol2024",  # Senha do usuário a ser criada
    "administrador": "true"  # Define se o usuário é um administrador
}

