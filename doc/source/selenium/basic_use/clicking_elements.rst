Clicando em elementos (``click``)
---------------------------------

Para clicar em elementos usamos o método ``click`` de ``WebElement``

.. code-block:: python

    link = driver.find_element(By.ID, 'js-link-box-en')
    link.click()

Se estivermos interessados em testar a página (e não apenas em automatizar) é interessante usar o texto do link em vez do id.

.. code-block:: python

    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'English')
    link.click()
