import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_logout(browser, base_url, wait, admin_creds):
    browser.get(f"{base_url}administration/index.php?route=common/login")

    """Вводим логин/пароль"""
    input_user = wait.until(EC.presence_of_element_located((By.ID, "input-username")))
    input_password = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    input_user.send_keys(admin_creds["login"])
    input_password.send_keys(admin_creds["password"])
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

    """Проверяем что попали в админку"""
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))).is_displayed()

    """Выходим из админки"""
    wait.until(EC.presence_of_element_located((By.ID, "nav-logout"))).click()

    """Проверяем, что вернулись на страницу авторизации"""
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),' Please enter your login details.')]"))).is_displayed()


def test_add_product_in_card(browser, base_url, wait):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en-gb/product/iphone']").click()
    browser.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]").click()
    browser.get(f"{base_url}en-gb?route=checkout/cart")
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'iPhone')]"))).is_displayed()


def test_check_change_price_mainpage(browser, base_url, wait):
    browser.get(base_url)
    """Получаем цены ДО смены валюты"""
    price_elements = browser.find_elements(By.CLASS_NAME, "price")
    prices_before = price_elements[0].text
    print("\nPrice before:", prices_before)

    """Меняем валюту"""
    browser.find_element(By.CSS_SELECTOR, "[data-bs-toggle='dropdown']").click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item").click()

    """Получаем цену ПОСЛЕ смены валюты"""
    price_elements = browser.find_elements(By.CLASS_NAME, "price")
    prices_after = price_elements[0].text
    print("Price after:", prices_after)

    """Проверяем, что цены поменялись"""
    assert prices_before != prices_after, "Prices have not changed on the main page!"
    print("Prices on the main page have changed")
