import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestFailedLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_failed_login(self):
        driver = self.browser  # Buka web browser
        driver.get("https://www.saucedemo.com/")  # Buka situs
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("")  # Isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # Validasi
        response_data = driver.find_element(By.CLASS_NAME, "error-message-container.error").text
        self.assertIn('Epic sadface: Username is required', response_data)
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
    