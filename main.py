#Imoorts
import os
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep
from interactor import Interactor



#Initializes browser
directory = input("Input directory: (syntax drive:/file/lo/cation)")

correct_answer = input("Input the correct answer value: ")
user_name = input("Username: ")      
password =  input("Password: ")

os.system('cls')
driver = webdriver.Edge()
action = ActionChains(driver)
question_input = Interactor()

#Opens browser link
driver.get("https://dashboard.blooket.com/my-sets")
question_input.interact_with(driver,action,1,'/html/body/main/div[2]/div[2]/form/div[1]/input',user_name) #click username
question_input.interact_with(driver,action,1,'/html/body/main/div[2]/div[2]/form/div[2]/input',password)  #click password
action.send_keys(Keys.RETURN).perform() #press enter
question_input.click(driver,1,'//*[@id="app"]/div/div/div[1]/a[6]')# click set maker

    #Xpaths for the inputs and buttons nececarry
xpath_list = [

   '//*[@id="app"]/div/div/div[7]/form/div[1]/div[2]/input', # title input 0
   '//*[@id="app"]/div/div/div[7]/form/div[3]/div',# create button  1
   '//*[@id="app"]/div/div/div[7]/div/div[1]/div[2]/div[1]', # add question 2
   '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[1]/div[2]',# question input 3 
   '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[1]/div/div[2]', # answer 1   4
   '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[2]/div/div[2]', # answer 2   5
   '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[3]/div/div[2]',# answer 3    6  
   '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[2]', # answer 4   7
   f'/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[{correct_answer}]/div/div[1]/div[1]', # answer  1 check 8
  # '/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[2]/div/div[1]/div[1]',#answer 2 check
   #'/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[3]/div/div[1]/div[1]' # answer 3 check 
   #'/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[1]/div[1]', # answer 4 check
   '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[2]', #save  9
   '//*[@id="app"]/div/div/div[7]/div/div[1]/div[1]/div[5]',# save set  10
   '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[1]',#escape 11
   '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[1]/',#cancel 12
   '/html/body/main/div[2]/div[2]/form/div[2]/input',#input password 13
   '/html/body/main/div[2]/div[2]/form/div[1]/input',#input user
   '/html/body/div[1]/div/div/div[1]/a[6]'#create set
   '//*[@id="app"]/div/div/div[1]/a[6]' #set creator
    ]

#opens the directory and iterates through it like a list of files
for files in os.listdir(directory):
    name = files.split()
    
    name.remove('.txt') #removes .txt from the name
    name = ' '.join(name)
    # name = input("Blooket Name: ")
    answer_index =0 
    #Opens the file and turns it into a list
    with open (directory+files,'r',encoding='utf-8') as questions:
        list_of_questions = questions.readlines()    
        questions.close()

    #remove the /n and turn it into ''
    for values in range(len(list_of_questions)):
        list_of_questions[values] = list_of_questions[values].split()
        list_of_questions[values] = ' '.join(list_of_questions[values])

    question_input.interact_with(driver,action,1,xpath_list[0],name) #input title
    question_input.click(driver, 1 ,xpath_list[1]) # Click create button 
    question_input.click(driver, 1 ,xpath_list[2]) # add question
    for values in range(len(list_of_questions)):
      if list_of_questions[values] != '':
            print(list_of_questions[values])
            question_input.interact_with(driver,action,1,xpath_list[3+answer_index], list_of_questions[values])
            answer_index+=1 #Used as a sneaky work around to my lack of skill
            if  list_of_questions[values+1] == '' and  list_of_questions[values+2] == '' :

              question_input.click(driver, 1 ,xpath_list[8]) #click correct answer
              question_input.click(driver, 1 ,xpath_list[9]) #click save
              question_input.click(driver, 1 ,xpath_list[2]) #click add question
              answer_index =0
               
               
               

    question_input.click(driver, 4 , xpath_list[10] )  # Save set
    question_input.click(driver, 4 , xpath_list[15] )  # Create set
    
