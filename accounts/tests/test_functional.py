from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def testform(server, live_server):
    """
    Get the URL, then find forms fields and submit button by element id
    Forms fields are then filled with send keys
    """
    server.get(live_server.url + '/accounts/signup/')

    first_name = server.find_element(By.ID, 'id_first_name')
    last_name = server.find_element(By.ID, 'id_last_name')
    email = server.find_element(By.ID, 'id_email')
    birth_date = server.find_element(By.ID, 'id_birth_date')
    id_password1 = server.find_element(By.ID, 'id_password1')
    id_password2 = server.find_element(By.ID, 'id_password2')

    submit = server.find_element(By.ID, 'submit_button')

    first_name.send_keys('Jean')
    last_name.send_keys('Bon')
    email.send_keys('test@test.com')
    birth_date.send_keys('2000-12-12')
    id_password1.send_keys('helloworld')
    id_password2.send_keys('helloworld')

    submit.send_keys(Keys.RETURN)

    assert 'Jean' in server.page_source
    assert 'test@test.com' in server.page_source
