from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By


def driver_setup():
  options = ChromeOptions()
  service = ChromeService(ChromeDriverManager().install())
  options.add_experimental_option('detach', True)
  driver = webdriver.Chrome(service=service, options=options)
  return driver


if __name__ == '__main__':

    print(__name__)
    my_driver =  driver_setup()
    driver = my_driver.get('http://testphp.vulnweb.com/login.php')
    username = my_driver.find_element(By.NAME,'uname')
    username.send_keys('test')
    password_input = my_driver.find_element(By.NAME,'pass')
    password_input.send_keys("test")
    login_botton = my_driver.find_element(By.CSS_SELECTOR,'input[value="login"]').click()





