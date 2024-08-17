# Etapa II - Automação de Teste Web I
# Aplicação alvo: buscacep.correios.com.br

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnderecoBemol:
    def __init__(self, driver):
        self.driver = driver

    # Localziar elementos da página
    campo_busca = (By.NAME, "relaxation") # com base na linha 348 do codigo fonte da pagina
    botao_buscar = (By.XPATH, "//imput[@value='Buscar]")
    resultado_endereco = (By.XPATH, "//table[@class='tmptabela']//td[contains(text(), 'Rua Miranda Leão')]")

