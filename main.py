from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox(executable_path="D:\\Python\\geckodriver.exe")
driver.get("https://netpeak.ua/")
time.sleep(2)
step2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[4]/a')
step2.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(15)
step3 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[5]/div/a')
step3.click()
driver.save_screenshot("C:\\Users\\Winaared\\Desktop\\screenshot.png")
import pyautogui
step4 = driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[8]/div[1]/div[3]/button/i")
step4.click()
time.sleep(2)
pyautogui.write('C:\\Users\\Winaared\\Desktop\\screenshot.png')
pyautogui.press('enter')
time.sleep(5)


def checkstep4():
    try:
        driver.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[8]/div[2]/label')
    except NoSuchElementException:
        return False
    return True


print('step4= ')
print(checkstep4())
from random import choice
from string import ascii_uppercase
from string import digits
from selenium.webdriver.support.ui import Select
step51 = driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[10]/div[1]/div[1]/input")
step51.send_keys(''.join(choice(ascii_uppercase) for i in range(10)))
step52 = driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[10]/div[1]/div[2]/input")
step52.send_keys(''.join(choice(ascii_uppercase) for i in range(10)))
step53 = driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[10]/div[2]/input")
step53.send_keys(''.join(choice(ascii_uppercase) for i in range(10)))
step54 = Select(driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[2]/select"))
step54.select_by_visible_text('1984')
step55 = Select(driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[3]/select"))
step55.select_by_visible_text('января')
step56 = Select(driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[4]/select"))
step56.select_by_visible_text('1')
step57 = driver.find_element_by_xpath("/html/body/form/div[1]/div/div[1]/div[11]/div[5]/input")
step57.send_keys(''.join(choice(digits) for i in range(11)))
step6 = driver.find_element_by_xpath("/html/body/form/div[2]/button")
step6.click()
time.sleep(5)


def checkstep7():
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/p")
    except NoSuchElementException:
        return False
    return True


print('step7= ')
print(checkstep7())
step8 = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/div[2]/div/nav/ul/li[3]/a")
step8.click()
url = "https://school.netpeak.group/"
if driver.current_url == url:
    checkstep8="True"
else:
    checkstep8="False"


print('step8= ')
print(str(checkstep8))
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
