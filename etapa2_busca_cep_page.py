# Etapa II - Automação de Teste Web I
# Aplicação alvo: buscacep.correios.com.br

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnderecoBemol:
    def __init__(self, driver):
        self.driver = driver # para  intereção como navegador

    # Localziar elementos da página
    campo_busca = (By.NAME, "relaxation") # com base na linha 348 do codigo fonte da pagina localiza o atributo 'name'
    botao_buscar = (By.XPATH, "//input[@value='Buscar']") # procura um elemento de input com o valor 'Buscar'
    resultado_endereco = (By.XPATH, "//table[@class='tmptabela']//td[contains(text(), 'Manaus/AM')]") # locaiza um elemento com classe 'tmptabela' que contenha esse texto

    # Ações no navegador
    def preencher_campo_busca(self, valor):
        busca_input = WebDriverWait(self.driver, 10).until( # delay de 10 segundos para o carregamento da pagina
            EC.presence_of_element_located(self.campo_busca) # aguarda a presença do elemento localizado por campo_busca
        )
        busca_input.clear() # limpa o campo
        busca_input.send_keys(valor) # insere o valor desejado no campo de busca

    def clicar_buscar(self):
        selecionar_buscar = WebDriverWait(self.driver, 10).until( # delay de 10 seundos para a presença do botão Buscar
            EC.element_to_be_clickable(self.botao_buscar) # identifica o elemento a ser clicado
        )
        selecionar_buscar.click() # clica

    def obter_endereco(self):
        elemento_endereco = WebDriverWait(self.driver, 10).until( # delay de 10 segundos para que o elemento com o resultado do endereço esteja presente 
            EC.presence_of_element_located(self.resultado_endereco)
        )
        return elemento_endereco.text # Retorna o texto contido no elemento encontrado (o endereço em si)