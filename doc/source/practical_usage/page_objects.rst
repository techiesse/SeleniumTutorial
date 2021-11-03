Page Objects
============

Na prática não escrevemos o código de automação do navegador diretamente no script de testes.

Se fizermos isso vamos acabar com muito código repetido e não vamos conseguir reusar rotinas úteis de automação.

É melhor criar objetos que representem a página sendo automatizada e fazer todo acesso à página ser gerenciado por esse objeto.

.. code-block:: python

    # LoginPage.py
    class LoginPage:
        def __init__(self, driver):
            self.driver = driver

        def login(self, username, password):
            usernameInput = self.driver.find_element(By.ID, 'id_username')
            usernameInput.send_keys(username)

            usernameInput = self.driver.find_element(By.ID, 'id_password')
            usernameInput.send_keys(password)

            self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()


    # test.py
    def test_login():
        with webdriver.Chrome() as driver:
            loginPage = LoginPage(driver)
            loginPage.login(config.USERNAME, config.PASSWORD)

            assert driver.title = "My Profile" # Titulo da página que vem depois do login.

Não tem porque não fazer o page object bem expressivo:

.. code-block:: python

    # PageObjects.py
    class BasePage:
        def __init__(self, driver):
            self.driver = driver
            self._username_element = self.driver.find_element(By.ID, 'id_username')
            self._password_element = self.driver.find_element(By.ID, 'id_password')


    class LoginPage(BasePage):
        @property
        def username(self):
            return self._username_element.text

        @username.setter
        def username(self, value):
            return self._username_element.send_keys(value)

        @property
        def password(self):
            return self._password_element.text

        @password.setter
        def password(self, value):
            return self._password_element.send_keys(value)

        def submit(self):
            self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()

        def login(self, username, password):
            self.username = username
            self.password = password
            self.submit()


Referências:

- https://www.selenium.dev/documentation/guidelines/
- https://www.selenium.dev/documentation/guidelines/page_object_models/
