import os
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from interactor import Interactor

# Opens question file then extracts the info and closes it

#Initializes browser


directory = input("Input directory: (syntax drive:/file/lo/cation)")
question_count = 0
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Edge(options=options)
action = ActionChains(driver)
question_input = Interactor()
question_input.set_global_driver_and_action(driver,action)
#Opens browser link

start_time = time.time()

def blooket_maker(directory):
    correct_answer = 1 #input("Input the correct answer value: ")
    name =  input("Do you want to choose the names of the blookets: (Y/N) ")
    user_name = input("Username: ")      
    password = input("Password: ")
    os.system('cls')
    driver.get("https://dashboard.blooket.com/my-sets")
    question_input.interact_with(xpath='/html/body/main/div[2]/div[2]/form/div[1]/input',text_input = user_name)
    question_input.interact_with(xpath='/html/body/main/div[2]/div[2]/form/div[2]/input',text_input = password)
    action.send_keys(Keys.RETURN).perform()
    question_input.click(xpath='//*[@id="app"]/div/div/div[1]/a[6]')# click set maker

        #Xpaths for the inputs and buttons nececarry
    xpath_list = [

       '//*[@id="app"]/div/div/div[7]/form/div[1]/div[2]/input', # title input 0
       '//*[@id="app"]/div/div/div[7]/form/div[3]/div',# create button  1 
       '//*[@id="app"]/div/div/div[7]/div/div[1]/div[2]/div[1]', # add question 2
       '/html/body/div/div/div/div[8]/div/div/div[3]/div[1]/div[2]',# question input 3 /html/body/div/div/div/div[8]/div/div/div[3]/div[1]/div[2]
       '/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[1]/div/div[2]', # answer 1   4 /html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[1]/div/div[2]
       '/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[2]/div/div[2]', # answer 2   5 /html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[2]/div/div[2]
       '/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[3]/div/div[2]',# answer 3    6  //*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[3]/div/div[2]
       '/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[2]', # answer 4   7  //*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[2]
       f'/html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[{correct_answer}]/div/div[1]/div[1]', # answer  1 check 8 /html/body/div/div/div/div[8]/div/div/div[3]/div[2]/div[x]/div/div[1]/div[1]
       '/html/body/div/div/div/div[8]/div/div/div[2]/div[2]/div[2]', #save  9 //*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[2]
       '//*[@id="app"]/div/div/div[7]/div/div[1]/div[1]/div[5]',# save set  10 /html/body/div/div/div/div[7]/div/div[1]/div[1]/div[5]/div[3]
       '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[1]',#escape 11
       '/html/body/div/div/div/div[8]/div/div/div[2]/div[2]/div[1]',#cancel 12 /html/body/div/div/div/div[8]/div/div/div[2]/div[2]/div[1]
       '/html/body/main/div[2]/div[2]/form/div[2]/input',#input password 13
       '/html/body/main/div[2]/div[2]/form/div[1]/input',#input user
       '/html/body/div[1]/div/div/div[1]/a[6]'#create set
       '//*[@id="app"]/div/div/div[1]/a[6]' #set creator /html/body/div/div/div/div[1]/a[7]/div
        ]
    #opens all files in the directory and iterates through them
    for files in os.listdir(directory):
        cycle = 0 
        answer_index = 0 
        #name.remove('questions.txt')
        if name not in ['n','N','']:
                name = input("Choose a name: ")
        else:

            name = files.split()
            name = ' '.join(name)
        
        with open (directory+files,'r',encoding='utf-8') as questions:
            list_of_questions = questions.readlines()    
            questions.close()
         
        for values in range(len(list_of_questions)):
            list_of_questions[values] = list_of_questions[values].split()
            list_of_questions[values] = ' '.join(list_of_questions[values])

        question_input.interact_with(1,xpath_list[0],name) #input title
        question_input.click(  xpath= xpath_list[1]) # Click create button 
        question_input.click( xpath= xpath_list[2]) # add question
        global question_count
        
        for values in range(len(list_of_questions)):
                if list_of_questions[values] != '':
                    print(list_of_questions[values])
                    question_input.interact_with( xpath = xpath_list[3+answer_index], text_input = list_of_questions[values])
                    answer_index+=1
                   
                    try:
                        if  (list_of_questions[values+1] == '' and  list_of_questions[values+2] == '') :
                        
                            question_input.click(xpath = xpath_list[8]) #click correct answer
                            question_input.click(xpath = xpath_list[9]) #click save
                            answer_index =0
                            question_count+=1
                            if values+2 <= len(list_of_questions)-1 :
                                question_input.click( xpath = xpath_list[2]) #click add question
                    except IndexError:
                            question_count+=1
                            question_input.click(xpath = xpath_list[8]) #click correct answer
                            question_input.click(xpath = xpath_list[9]) #click save
        time.sleep(2)        
        question_input.click(xpath_list[10] )  # Save set
        cycle +=1
        if cycle < len(os.listdir(directory))  :
               time.sleep(2)
               question_input.click( xpath_list[15] )  # Create set
        print(f"Done making blooket called: {name} ")   
      
blooket_maker(directory)       
execution_time = time.time() - start_time
print(f"It took {execution_time} seconds to put {question_count} questions in the blooket(s) ")
