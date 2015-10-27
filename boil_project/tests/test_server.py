from unittest import skipIf

from django.test.testcases import LiveServerTestCase
from selenium.webdriver import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from boil_app.tests.test_views import create_pod


@skipIf(True, "Run selenium tests manually.")
class MySeleniumTests(LiveServerTestCase):
    selenium = None
    timeout = 1

    @classmethod
    def setUpClass(cls):
        myproxy = "http://rproxy.mcp.com:3128"

        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myproxy,
            'ftpProxy': myproxy,
            'sslProxy': myproxy,
            'noProxy': ''}
        )
        cls.selenium = WebDriver(proxy=proxy)

        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_index_page(self):
        self.selenium.get(u'{0:s}{1:s}'.format(self.live_server_url, '/'))

        # Wait until the response is received
        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body'))

    def test_pod_list(self):
        create_pod('adfa')
        self.selenium.get('{}{}'.format(self.live_server_url, '/lab/pods/'))

        WebDriverWait(self.selenium, self.timeout).until(
            lambda driver: driver.find_element_by_tag_name('body')
        )
        page_head = self.selenium.find_element_by_tag_name('h2')
        self.assertIn('Pod Info', page_head.text)
        # self.selenium.find_element_by_link_text(a.name).click()
        # body = self.selenium.find_element_by_tag_name('body')
        # self.assertIn(a.title, body.text)