import pytest

from django.test import Client as DjangoClient
from accounts.models import CustomUser
from products.models import Product

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def user(db):
    """Create a user"""
    user = CustomUser.objects.create_superuser(
        birth_date='1992-05-15',
        email='helloworld@hello.world',
        username='axel',
        password='test'
    )
    return user


@pytest.fixture
def connected_client(user):
    """Log in the user"""
    connected_client = DjangoClient()
    connected_client.force_login(user)
    return connected_client


@pytest.fixture()
def server(db):
    """Selenium web driver setup"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    selenium = webdriver.Chrome(service=service, options=chrome_options)
    selenium.implicitly_wait(10)
    return selenium


@pytest.fixture
def products_creation():
    product_1, _ = Product.objects.get_or_create(
        name='Test products',
        url='testurl.test',
        image_url='test.testimage.com',
        nutriscore='d',
        fat_100g='0.2',
        satured_fat_100g='0.85',
        sugar_100g='0.4',
        salt_100g='1.2'
    )
    product_2, _ = Product.objects.get_or_create(
        name='Test_products_2',
        url='testurl2.test2',
        image_url='test2.testimage2.com',
        nutriscore='d',
        fat_100g='0.4',
        satured_fat_100g='0.9',
        sugar_100g='1.4',
        salt_100g='1.5'
    )
    return product_1, product_2
