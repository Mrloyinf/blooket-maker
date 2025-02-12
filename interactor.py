#from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep



class Interactor():

    def set_global_driver_and_action(self,driver, action):
      
        '''

        This function initializes the variables driver and action      

        '''
        
        self.driver = driver
        self.action = action
    def interact_with(self,sleep_time = 0  ,xpath = 0,text_input = 0):
            
            '''
            
            This function first asks for a sleep time, then the xpath of the object, then the question text.
            
            '''
            
            interactable = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
            interactable.click()
            sleep(sleep_time)
            self.action.send_keys(text_input).perform()
    def click(self,sleep_time = 0, xpath = 0):
          
           '''

           This function asks for a sleep time, then xpath of the object to be clicked

           '''
           
           interactable = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
           sleep(sleep_time)
           interactable.click()





