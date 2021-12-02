from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Setup:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver
