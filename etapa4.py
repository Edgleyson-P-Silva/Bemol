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
