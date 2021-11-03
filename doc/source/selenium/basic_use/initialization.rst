Inicialização
-------------

.. code-block:: python

    from selenium import webdriver

    driver = webdriver.Chrome()

    # Meu código de automação

    driver.quit()

Ou melhor, usando um context manager

.. code-block:: python

    from selenium import webdriver

    with webdriver.Chrome as driver:
        # Meu código de automação
