from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture()
def setUp():
    global name,yop,dirname,dist,producer,driver
    name=input("enter name")
    yop=input("enter year")
    dirname=input("enter dirname")
    dist=input("enter distname")
    producer=input("enter prodname")

    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(name)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yop)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(dirname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(dist)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(2)
