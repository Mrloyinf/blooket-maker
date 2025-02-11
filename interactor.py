#from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep



class Interactor():

    def __init__(self):
        
        self.driver = ''
    def interact_with(self,driver_input,action_keys,sleep_time  ,xpath,question):
            '''
            
             This function first asks for a driver,then the action keys, then how fast it should type, then the xpath of the object, then the question text
             
            '''
            
            self.driver = driver_input
            interactable = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
            interactable.click()
            sleep(sleep_time)
            action_keys.send_keys(question).perform()
    def click(self,driver,sleep_time , xpath):
           '''

           This function asks for a type speed, then xpath of the object to be clicked

           '''
           self.driver = driver
           interactable = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
           sleep(sleep_time)
           interactable.click()






