from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def ex01():
    with webdriver.Chrome() as driver:
        driver.get('https://wikipedia.org')
        h1 = driver.find_element(By.TAG_NAME, 'h1')
        time.sleep(1)
        print(h1.text)

        languages_container = driver.find_element(By.XPATH, '//div[@class="central-featured"]')
        language_elements = languages_container.find_elements(By.XPATH, 'div/a/strong')
        for language_element in language_elements:
            print(language_element.text)

        # Click no link para WP em inglês
        #link = driver.find_element(By.ID, 'js-link-box-en')
        link = driver.find_element(By.PARTIAL_LINK_TEXT, 'English')
        link.click()

        # Obter e preencher o campo de busca:
        searchInputElement = driver.find_element(By.XPATH, 'input[@type="search"]')
        searchInputElement.send_keys('the text book')

        # Obter e clicar no botão de submit:
        submitButton = driver.find_element(By.XPATH, 'button[@type="submit"]')
        submitButton.click()

        input('Pressione ENTER para continuar ...')

def ex02():
    with webdriver.Chrome() as driver:
        driver.get('https://wikipedia.org')
        h1 = driver.find_element(By.TAG_NAME, 'h1')
        time.sleep(1)
        print(h1.text)

        # Obter e preencher o campo de busca:
        searchInputElement = driver.find_element(By.XPATH, '//input[@type="search"]')
        searchInputElement.send_keys('the tex book')

        # Obter e clicar no botão de submit:
        submitButton = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submitButton.click()

        title = driver.execute_script('return document.title')
        print(f'Título: {title}')

        input('Pressione ENTER para continuar ...')

if __name__ == '__main__':
    ex02()
