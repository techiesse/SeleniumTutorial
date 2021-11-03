Localizando Elementos em uma Página (``find_element[s]``)
---------------------------------------------------------

A partir do objeto ``driver`` podemos navegar na página e localizar os elementos que desejamos

.. code-block:: python

    from selenium.webdriver.common.by import By

    h1 = driver.find_element(By.TAG_NAME, 'h1')
    print(h1.text)

O método ``find_element`` retorna um ``WebElement`` que representa um elemento do DOM da página. Além de conter os atributos do elemento encontrado ele também permite chamar ``find_element`` sobre si mesmo para fazer uma busca sobre os filhos

.. warning::

    Cuidado ao usar ``By.XPATH`` em ``element.find_element`` pois padrões globais vão fazer com que a busca não se restrinja ao elemento atual

Podemos por exemplo obter a lista de linguagens exibidas na homepage:

.. code-block:: python

    languagesContainer = driver.find_element(By.XPATH, '//div[@class="central-featured"]')
    languageElements = languagesContainer.find_elements(By.XPATH, './div/a/strong')
    for languageElement in languageElements:
        print(languageElement.text)
