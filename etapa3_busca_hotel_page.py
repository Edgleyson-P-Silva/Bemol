from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuscaHotelTrivago:
    def __init__(self, driver):
        self.driver = driver # para  intereção como navegador

    # Localizar elementos na página
    campo_busca = (By.CSS_SELECTOR, "input[placeholder='Para onde?']")
  
