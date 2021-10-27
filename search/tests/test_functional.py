from selenium.webdriver.common.by import By


def test_autocompletion(server, products_creation, live_server):
    """
    Create two products, find the search bar by ID and write beginning of
    product name in it. Then we find the new autocompletion element and
    we check if the product names are in there.
    """
    server.get(live_server.url)

    product_1, product_2 = products_creation
    search_bar = server.find_element(By.ID, 'product')
    search_bar.send_keys('Test')
    autocompletion_names = server.find_elements(By.CLASS_NAME, 'ui-menu-item')

    assert 'Test' in autocompletion_names[0].text
    assert 'Test_products_2' in autocompletion_names[1].text
