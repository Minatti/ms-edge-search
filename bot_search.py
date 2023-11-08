from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time


path_to_profile = "C:\\Users\\workcarminatti\\AppData\\Local\\Microsoft\\Edge\\User Data1\\"
path_to_webdriver = "C:\\webdrivers\\msedgedriver.exe"  # Substitua pelo caminho correto do driver

# Configurar as opções do Microsoft Edge
edge_options = Options()
#edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
edge_options.add_argument(f'--user-data-dir={path_to_profile}')

# Inicializar o serviço do Microsoft Edge WebDriver
service = Service(path_to_webdriver)

# Inicializar o driver do Microsoft Edge
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()


get_api_text = 'É uma ferramenta gratuita que permite gerar frases e citações escolhidas ao acaso de um vasto banco de dados.Quer fazer um post ou um tweet, mas está sem ideias? Chegou ao sítio certo. No mil-frases criamos o gerador de frases aleatorias para ser facil gerar uma frase ao acaso e ter sempre bons resultados. Basta escolher a categoria pretendida e poderá gerar tantas frases quanto quiser. Para utilizar esta ferramenta, basta clicar no botão "Obter nova frase Aleatória" e uma nova citação será exibida na tela. O Mil-Frases também oferece a opção de gerar citações de autores específicos ou frases sobre temas específicos, bastando selecionar as opções desejadas antes de clicar no botão de geração de frases. Além disso, o Mil-Frases permite que as frases geradas sejam compartilhadas nas redes sociais ou baixadas em formato de imagem.'


print('acessar site')
driver.get('https://www.bing.com/')
time.sleep(3)
print('localizar alvo da pesquisa')
search_box = driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
print('clicar no alvo')
search_box.click()
print('esperar 2s')
time.sleep(2)
print('colar texto')
search_box.send_keys(get_api_text)
print('pressionar enter')
search_box.send_keys(Keys.ENTER)
time.sleep(2)


while True: 
    print('busca alvo')
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
    print('apaga')
    search_box.send_keys(Keys.BACKSPACE)
    time.sleep(3)
    print('pesquisa')
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)






