from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class test_saucedemo:
    def test_username_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(3)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Boş Test Sonuç: {testResult}")

    def test_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("Mehmet")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(3)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Şifre Boş Sonuç: {testResult}")

   
    def test_error(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Hatalı Sonuç: {testResult}")

    def test_numberOfLists(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")    
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID ,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(3)
        passwordInput = driver.find_element(By.ID ,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        listOfCourses = driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(listOfCourses) == 6
        print(f"TEST SONUCU: {testResult}")


testClass = test_saucedemo()
testClass.test_username_password_empty()
testClass.test_password_empty()
testClass.test_error()
testClass.test_numberOfLists()