Preenchendo formulários (``send_keys``)
---------------------------------------

Para fazer uma pesquisa podemos usar o método ``send_keys`` em um elemento que aceite entrada de dados (tag ``input`` por exemplo)

.. code-block:: python

    # Obter e preencher o campo de busca:
    searchInputElement = driver.find_element(By.XPATH, '//input[@type="search"]')
    searchInputElement.send_keys('the tex book')

    # Obter e clicar no botão de submit:
    submitButton = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submitButton.click()
