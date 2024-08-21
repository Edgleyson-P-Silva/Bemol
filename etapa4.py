<<<<<<< Updated upstream
import unittest 
import requests #requisicoes http para ineragir com a api

class TestServerestAPI(unittest.TestCase):

    def setUp(self):
        self.url_base = "https://serverest.dev"

    def criar_usuario(self):
        novo_usuario = {
            "nome": "Edgleyson Silva",
            "email": "edgleyson99@outlook.com",
            "password": "qaenginnerbemol2024",
            "administrador": "true"
        }

    def login(self):
        dados_login = {
            "email": "edgleyson99@outlook.com", 
            "password": "qaenginnerbemol2024"
        }
=======
import requests #requisicoes http para ineragir com a api

url_base = "https://serverest.dev"
headers = HEADERS = {"Content-Type": "application/json"}  # Cabeçalhos HTTP em json

usuario = {
    "nome": "Edgleyson Silva",  # Nome do usuário a ser criado
    "email": "edgleyson99@outlook.com",  # Email do usuário a ser criado
    "password": "qaenginnerbemol2024",  # Senha do usuário a ser criada
    "administrador": "true"  # Define se o usuário é um administrador
}

>>>>>>> Stashed changes
