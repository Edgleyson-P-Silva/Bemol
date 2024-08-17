from selenium import webdriver
from etapa2_busca_cep_page import EnderecoBemol
import time

driver = webdriver.Chrome() # configurar WebDriver para o Chrome

# o site "https://buscacep.correios.com.br/" não carregava e o primeiro resultado para busca de CEP encontrado no google envolvia captcha, entao usei o endereço abaixo:
driver.get("https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm")

page = EnderecoBemol(driver)

# Cenário 1: Buscar por CEP 69005-040
page.preencher_campo_busca ("69005040")
page.clicar_buscar()
endereco = page.obter_endereco()
assert "Rua Miranda Leão" in endereco

# Aguarda 10 segundos antes de fechar o navegador
time.sleep(10)

# Fecha o navegador
driver.quit()