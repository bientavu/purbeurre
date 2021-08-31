from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your tests here.
class UserFormTest(LiveServerTestCase):

    def testform(self):
        selenium = webdriver.Chrome()
        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/accounts/signup/')
        # find the elements you need to submit form
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        email = selenium.find_element_by_id('id_email')
        birth_date = selenium.find_element_by_id('id_birth_date')
        id_password1 = selenium.find_element_by_id('id_password1')
        id_password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_class_name('submit_button')

        # populate the form with data
        first_name.send_keys('Jean')
        last_name.send_keys('Bon')
        email.send_keys('test@test.com')
        birth_date.send_keys('2000-12-12')
        id_password1.send_keys('helloworld')
        id_password2.send_keys('helloworld')

        # submit form
        submit.send_keys(Keys.RETURN)

        # check result; page source looks at entire html document
        assert 'Jean' in selenium.page_source
