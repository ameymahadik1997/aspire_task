from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def waitForLoad(path,sec):
    WebDriverWait(driver,sec).until(EC.presence_of_all_elements_located((By.XPATH,path)))

try:
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    username = "user@aspireapp.com"
    password = "@sp1r3app"
    productFieldName = "The Kington Brush"

    driver.get("https://aspireapp.odoo.com")
    

    time.sleep(2)
    loginBox = driver.find_element_by_xpath('//*[@id="login"]')
    loginBox.send_keys(username)

    passBox = driver.find_element_by_xpath('//*[@id="password"]')
    passBox.send_keys(password)

    loginButton = driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/div/div/div/form/div[3]/button')
    loginButton.click()


    # Need to go the inventory
    # Need to wait till the page with inventory opens up
    waitForLoad('//*[@id="result_app_1"]/div[1]',30)
    inventoryButton = driver.find_element_by_xpath('//*[@id="result_app_1"]/div[1]')
    inventoryButton.click()
    time.sleep(3)
    # Goin to the product button on the Menu
    productsButtonMenu = driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li[3]/a').click()
    time.sleep(3)
    # Going to the product button inside the products Menu
    productButtonInside = driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li[3]/div/a[1]/span').click()
    time.sleep(3)

    # Need to wait till the page with creating an object opens up
    waitForLoad('/html/body/div[4]/div/div[1]/div[2]/div[1]/div/div/button',10)
    createButton = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div/div/button').click()
    time.sleep(3) 

    # Need to wait for the Adding the product information comes
    waitForLoad('//*[@id="o_field_input_736"]',10)
    productName = driver.find_element_by_xpath('//*[@id="o_field_input_736"]')
    productName.send_keys(productFieldName)  

    upgradeQuantity = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]/div/button[2]/span').click()

    # #Need to wait to add new element with quantity
    waitForLoad('/html/body/div[4]/div/div[1]/div[2]/div[1]/div/div/button[3]',5)
    createInsideQuantity = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div/div/button[3]').click()
    waitForLoad('/html/body/div[4]/div/div[2]/div/div[1]/table/thead/tr/th[2]',5)
    locationField = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div/div/input').send_keys("Random")
    print("Check Print Dropdown")
    # locationFieldSelect = driver.find_element_by_xpath('//*[@id="ui-id-18"]').click()
    # packageField = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div/div/input').click()
    # packageField.send_keys(15)
    # onHandQuantity = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[4]/input')
    # onHandQuantity.send_keys(10.00)
    # saveButton = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/div[1]/div/div/button[1]').click()

    print("Process of updating is completed")


    



    time.sleep(5)
    print("Closing the Website now")
    # driver.close()
except Exception as err:
    print("The error was occurred because of the following issue :- ",err)
    # driver.close()