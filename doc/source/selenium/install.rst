Instalação
==========

Selenium
--------

É recomendável inicialmente criar um ambiente virtual para o nosso projeto Python. ``pyenv`` ou ``virtualenvwrapper`` são opções válidas. Aqui vamos usar o ``virtualenv`` para facilitar o setup

.. code-block:: bash

    $ mkdir my_selenium_project
    $ cd my_selenium_project
    $ pip install virtualenv   # Instalando virtualenv globalmente
    $ virtualenv venv          # Criar o virtualenv colocando colocando o conteudo na pasta "my_selenium_project/venv"

Agora ativamos o virtualenv e instalamos o Selenium localmente nele:

.. code-block:: bash

    $ source venv/bin/activate # No windows: venv\Scripts\activate
    $ pip install selenium


ChromeDriver
------------

ChromeDriver é a implementação do Webdriver para o navegador Chrome.

A instalação do ChromeDriver é bem simples: Basta baixar o binário e colocá-lo no PATH ou no mesmo diretório onde o nosso script de automação será executado.

Link para o ChromeDriver: https://chromedriver.chromium.org/downloads

Após baixar o binário para a sua versão do Chrome colocar o mesmo em algum lugar acessível no PATH do sistema. No Linux um bom lugar costuma ser ``~/.local/bin``.
