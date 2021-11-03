Projetos de Teste
=================

É importante ter alguma ferramenta que facilite a execução de testes automatizados. Para projetos em Python o ``pytest`` é uma ferramenta bastante simples e conveniente para gerenciar a execução dos testes.

Exemplo de um Projeto com Pytest
--------------------------------

.. code-block:: python

    # test_simulation_page.py
    from selenium import webdriver
    from PageObjects import LoginPage, SimulationPage

    import config

    class TestSimulationPageAccess:
        def test_access_requires_authentication(self):
            with webdriver.Chrome() as driver:
                simulation_page = SimulationPage(driver)
                simulation_page.goto()
                assert driver.current_url == LoginPage.URL

        def test_allows_authenticated_access(self):
            with webdriver.Chrome() as driver:
                login_page = LoginPage(driver)
                login_page.login(config.USERNAME, config.PASSWORD)

                simulation_page = SimulationPage(driver)
                simulation_page.goto()
                assert driver.current_url == SimulationPage.URL


    ...

O script acima com ``pytest`` é executado simplesmente assim:

.. code-block:: bash

    $ pytest .

Uma vez que os arquivos, classes e métodos tenham sido escritos seguindo o padrão definido pelo ``pytest`` eles serão encontrados e executados corretamente.
