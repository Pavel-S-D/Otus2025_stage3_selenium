import pytest
from time import sleep


def test_part1(browser, base_url):
    browser.get(base_url)
    sleep(3)
