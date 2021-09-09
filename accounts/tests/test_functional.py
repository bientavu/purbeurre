from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class UserFormTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(ChromeDriverManager().install())
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testform(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        # self.selenium.get('http://127.0.0.1:8000/accounts/signup/')

        first_name = self.selenium.find_element_by_id('id_first_name')
        last_name = self.selenium.find_element_by_id('id_last_name')
        email = self.selenium.find_element_by_id('id_email')
        birth_date = self.selenium.find_element_by_id('id_birth_date')
        id_password1 = self.selenium.find_element_by_id('id_password1')
        id_password2 = self.selenium.find_element_by_id('id_password2')

        submit = self.selenium.find_element_by_id('submit_button')

        first_name.send_keys('Jean')
        last_name.send_keys('Bon')
        email.send_keys('test@test.com')
        birth_date.send_keys('2000-12-12')
        id_password1.send_keys('helloworld')
        id_password2.send_keys('helloworld')

        submit.send_keys(Keys.RETURN)

        assert 'Jean' in self.selenium.page_source
        assert 'test@test.com' in self.selenium.page_source
