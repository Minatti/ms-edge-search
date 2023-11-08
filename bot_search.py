from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time



#aplicando POO

class BotEdge():
    def __init__(self, path_to_profile, path_to_webdriver):
        self.path_to_profile = None
        self.path_to_webdriver = None
        self.edge_options = Options()
        self.edge_options.add_argument(f'--user-data-dir={path_to_profile}')
        self.service = Service(path_to_webdriver)
        self.driver = webdriver.Edge(service=self.service, options=self.edge_options)
        self.driver.maximize_window()

    #metodo para acessar site
    def open_bing(self):
        self.driver.get('https://www.bing.com/')

    def write_text(self, text):
        search_field = self.driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
        search_field.send_keys(text)

    def interaction_text(self):
        time.sleep(0.6)
        search_field = self.driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
        time.sleep(0.7)
        search_field.send_keys(Keys.BACK_SPACE)
        time.sleep(0.8)
        search_field.send_keys(Keys.ENTER)


# configs
path_to_profile = [
                    "C:\\Users\\workcarminatti\\AppData\\Local\\Microsoft\\Edge\\User Data1\\",
                    "C:\\Users\\workcarminatti\\AppData\\Local\\Microsoft\\Edge\\User Data2\\"
                   ]
path_to_webdriver = "C:\\webdrivers\\msedgedriver.exe"  # Substitua pelo caminho correto do driver


text = 'É uma ferramenta gratuita que permite gerar frases e citações escolhidas ao acaso de um vasto banco de dados.Quer fazer um post ou um tweet, mas está sem ideias? Chegou ao sítio certo. No mil-frases criamos o gerador de frases aleatorias para ser facil gerar uma frase ao acaso e ter sempre bons resultados. Basta escolher a categoria pretendida e poderá gerar tantas frases quanto quiser. Para utilizar esta ferramenta, basta clicar no botão "Obter nova frase Aleatória" e uma nova citação será exibida na tela. O Mil-Frases também oferece a opção de gerar citações de autores específicos ou frases sobre temas específicos, bastando selecionar as opções desejadas antes de clicar no botão de geração de frases. Além disso, o Mil-Frases permite que as frases geradas sejam compartilhadas nas redes sociais ou baixadas em formato de imagem.'

# criando uma nova instancia
jarbinhas = BotEdge(path_to_profile[0], path_to_webdriver)

# print('acessar site')
jarbinhas.open_bing()
time.sleep(0.4)

# print('digitar texto no campo')
jarbinhas.write_text(text)
time.sleep(0.6)



idgato = BotEdge(path_to_profile[1], path_to_webdriver)
idgato.open_bing()
time.sleep(0.5)
idgato.write_text(text)

while True:
    jarbinhas.interaction_text()
    idgato.interaction_text()





