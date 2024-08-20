from selenium import webdriver
from etapa3_busca_hotel_page import BuscaHotelTrivago  
import time

# Configuração do WebDriver
driver = webdriver.Chrome() # configurar WebDriver para o Chrome
driver.get("https://www.trivago.com.br/")

# criar instância da página
page = BuscaHotelTrivago(driver)

# Cenário: Buscar hotel em Manaus e ordenar por avaliação
destino = "Manaus"
time.sleep(1)
page.preencher_busca(destino)
time.sleep(5)
page.clicar_pesquisar()
time.sleep(5)
page.clicar_pesquisar()
time.sleep(5)

# Ordenar por avaliação e sugestões
time.sleep(10)
page.clicar_botao_ordenar()
time.sleep(3)
page.selecionar_opcao_avaliacao_e_sugestoes()
time.sleep(5)

# Obter informações do primeiro resultado
primeiro_resultado = page.obter_primeiro_resultado()
nome_hotel = page.obter_nome_hotel(primeiro_resultado)
avaliacao = page.obter_avaliacoes()
#avaliacao_nota = page.obter_nota()
preco = page.obter_preco(primeiro_resultado)

# Imprimir resultados
print(f"Hotel: {nome_hotel}")
print(f"Avaliação: {avaliacao} estrelas")
#print(f"Avaliação em nota: {avaliacao_nota}")
print(f"Preço: {preco}")

driver.execute_script(f"alert('Hotel {nome_hotel} com {avaliacao} estrelas e com o preço de {preco}');")
time.sleep(10)

# Fechar o navegador
driver.quit()
