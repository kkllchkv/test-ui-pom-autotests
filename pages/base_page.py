import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC

class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_path = None
    timeout = 30

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.actions = ActionChains(self.driver)

    def open_page(self):
        if self.page_path:
            self.driver.get(f'{self.base_url}{self.page_path}')
        else:
            raise ValueError('Required "page_path" parameter is missing')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_to_appear(self, locator):
        self.wait.until(
            EC.presence_of_element_located(locator)
                   )

    def wait_until_reload(self, element):
        self.wait.until(
            EC.staleness_of(element)
        )

    def wait_until_element_not_have_text(self, locator, text):
        self.wait.until_not(
            EC.text_to_be_present_in_element_attribute(locator, 'innerText', text)
                   )

    def wait_until_window_is_ready(self):
        """
        метод ожидает загрузки odoo обработчиков

        некоторые элементы страниц, например чекбоксы или строка поиска, работают в связке
        с обработчиками из odoo. до момента, пока браузер не подгрузит эти обработчики,
        автоматические редиректы на новые страницы (добавление query параметров, например,
        при фильтрации по чекбоксам) работать не будут
        """

        self.wait.until(
            lambda driver: self.driver.execute_script(
                """
                return Boolean(
                    window.odoo &&
                    window.odoo.__WOWL_DEBUG__ &&
                    window.odoo.__WOWL_DEBUG__.root
                )
                """
            ), message="Couldn't initialize core elements of the app. Timeout exceeded"
        )

    def find_at_shadow_root(self, shadow_root, locator):
        return shadow_root.find_element(*locator)

    def assure_page_has_loaded(self, expected_path, retry_count=2, timeout=3):
        for _ in range(retry_count):
            path = self.driver.execute_script("return window.location.pathname")
            try:
                assert expected_path == path
                return True
            except AssertionError:
                time.sleep(timeout)

        raise AssertionError(f"Couldn't open page with '{self.page_path}' path")
