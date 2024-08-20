from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuscaHotelTrivago:
    def __init__(self, driver):
        self.driver = driver # para  intereção como navegador

    # Localizar elementos na página
    campo_busca = (By.CSS_SELECTOR, "input[data-testid='search-form-destination']")
    botao_pesquisar = (By.CSS_SELECTOR, "[data-testid='search-button-with-loader']")
    botao_ordenar = (By.CSS_SELECTOR, "[data-testid='sorting-selector-select']")
    opcao_avaliacao_sugestao = (By.CSS_SELECTOR, "option[value='6']")
    primeiro_resultado = (By.CSS_SELECTOR, "button[data-testid='item-name']")
    avaliacao_estrela = (By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
    avaliacao_nota = (By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
    preco = (By.CSS_SELECTOR, "div[data-testid='expected-price'] span b")

  
