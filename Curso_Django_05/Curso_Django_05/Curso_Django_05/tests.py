from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:/Users/feoxp7/Desktop/Códigos/Cursos_Django/Curso_Django_05/chromedriver_win32/chromedriver.exe")

    def tearDown(self):
        self.browser.quit()




    def test_buscando_um_novo_animal(self):
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, 'exemplo')
        self.assertEqual('Busca animal',brand_element.text)
            
        

