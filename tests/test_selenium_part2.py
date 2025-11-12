import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main(browser, base_url, wait):
    browser.get(base_url)
    wait.until(EC.visibility_of_element_located((By.ID, "logo"))).is_displayed()
    wait.until(EC.presence_of_element_located((By.NAME, "search"))).is_displayed()


def test_check_catalog(browser, base_url, wait):
    browser.get(f"{base_url}en-gb/catalog/tablet")
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Tablet')]"))).is_displayed()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "img-fluid"))).is_displayed()


def test_prod_page(browser, base_url, wait):
    browser.get(f"{base_url}en-gb/product/tablet/samsung-galaxy-tab-10-1")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.price-new"))).is_displayed()
    wait.until(EC.presence_of_element_located((By.ID, "button-cart"))).is_displayed()
    button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    button.click()


def test_login_page(browser, base_url, wait):
    browser.get(f"{base_url}en-gb?route=account/login")
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'New Customer')]"))).is_displayed()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label.col-form-label"))).is_displayed()


def test_register_account_page(browser, base_url, wait):
    browser.get(f"{base_url}en-gb?route=account/register")
    wait.until(EC.presence_of_element_located((By.ID, "form-register"))).is_displayed()
    wait.until(EC.presence_of_element_located((By.XPATH, "//legend[contains(text(),'Your Password')]"))).is_displayed()
