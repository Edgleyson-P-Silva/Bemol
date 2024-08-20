from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuscaHotelTrivago:
    def __init__(self, driver):
        self.driver = driver # para  intereção como navegador

    # Localizar elementos na página
    campo_busca = (By.CSS_SELECTOR, "input[data-testid='search-form-destination']")
    botao_pesquisar = (By.CSS_SELECTOR, "button[data-testid='search-button-with-loader']") 
    opcao_avaliacao_sugestao = (By.CSS_SELECTOR, "option[value='6']")
    primeiro_resultado = (By.CSS_SELECTOR, "button[data-testid='item-name']")
    avaliacao_estrela = (By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
    avaliacao_nota = (By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
    preco = (By.CSS_SELECTOR, "div[data-testid='expected-price'] span b")
  
    # Ações
    def preencher_busca(self, destino):
        busca_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.campo_busca)
        )
        busca_input.clear()
        busca_input.send_keys(destino)

    def clicar_pesquisar(self):
        buscar_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_pesquisar)
        )
        buscar_button.click()

    def clicar_botao_ordenar(self):
        botao_ordenar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_ordenar)
        )
        botao_ordenar.click()

    def selecionar_opcao_avaliacao_e_sugestoes(self):
        opcao = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.opcao_avaliacao_sugestao)
        )
        opcao.click()

    def obter_primeiro_resultado(self):
        primeiro_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.primeiro_resultado)
        )
        return primeiro_elemento

    def obter_nome_hotel(self, elemento):
        return elemento.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text

    def obter_avaliacoes(self):
        nota_estrela = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.avaliacao_estrela)
        )
        return nota_estrela.get_attribute("content")

    def obter_preco(self, elemento):
        preco_valor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.preco)
        )
        return preco_valor.text
