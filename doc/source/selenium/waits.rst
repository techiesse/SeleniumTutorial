Esperando Condições ou Carga de Elementos
=========================================

Existem momentos em que o elemento que desajamos ler em uma página demora para ser carregado, seja  porque o servidor está demorando a responder uma requisição ou o próprio front end está demorando para renderizar a página. Neste caso, precisamos de mecanismos para aguardar a carga dos elementos e obter o comportamento desejado da automação.

Wait Implícito
--------------

Com um wait implícito, o WebDriver faz um polling no DOM durante um tempo tentando achar o elemento. É útil para aguardar elementos que não imediatamente disponíveis na página e precisam de um tempo para carregar.

.. code-block:: python

    driver.implicitly_wait(5) # Tempo é passado em segundos
    driver.find_element(By.TAG_NAME, 'p') # Se o elemento não existir no
    # momento da chamada da função o Webdriver vai esperar a carga

O wait implícito vai servir para todas as consultas feitas do momento em que são definidos até o final da sessão

Wait Explícito
--------------

Pode-se se definir um wait explícito para ter maior controle sobre exatamente o que aguardar evitando o efeito mais global do wait implícito.

.. code-block:: python

    from selenium.webdriver.support.ui import WebDriverWait

    wait = WebDriverWait(driver)
    el = wait.until(lambda d: d.find_element(By.TAG_NAME, 'p'))

A função passada para o ``until`` deve retornar algum valor que possa ser avaliado como verdadeiro (truthy), (em Python algo diferente de ``None``, ``False``, ``""``, ``[]`` e ``{}``)

O ``until`` irá tentar a condição algumas vezes e irá tentar achar o elemento quando a condição for "verdadeira".

.. note::

    O ``until`` irá retornar o mesmo objeto que for retornado pela função que avalia a condição (callback para testar a condição do wait). Pode-se aproveitar disso para retornar diretamente o resultado do ``until`` quando o mesmo retornar com sucesso.
