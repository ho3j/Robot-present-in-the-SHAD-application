"""
Hossein Jalili
feb-13-2022
version 1.0.0
Robot present in the SHAD application
"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import jdatetime


clear=lambda : os.system("cls")
now = jdatetime.datetime.now()
i=1

clear()
while True:
    # clear()
    print(now)
    print("---------------- try",str(i)," -----------------")
    number=input('\nplease enter your number: 9370000000\n')
    print('\nyour number is: '+number,"\n")
    if number.isdigit()==False:
        clear()
        print('\nplease enter a valid number(0-9)\n')
        i += 1  
    else:
        if len(number)==10:
            break
        else:
            i += 1
            clear()
            print('\nplease enter a valid 10_number (9370000000)\n')   
#----------------------------------------------

massage=input('please enter your massage: \n')
if massage=="":
    massage="Salam,sobh bekheir Ostad , mn hazer hastam"
else:
    pass
print(massage)
print("\n")
#----------------------------------------------

time_sendd=input('please enter your time:(09:28) \n')
names=input('please enter your name: \n')
if names=="" and time_sendd=="":
    print("can't find your name and time")
    exit()

#----------------------------------------------

try:
    path = os.path.dirname(os.path.abspath(__file__))
    address=os.path.join(path, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=address)
    driver.get('https://web.shad.ir/#/login')
except:
    print("can't connect to server")
    exit()

try:
    time.sleep(1)
    usernsme=driver.find_element_by_xpath('/html/body/div[1]/app-root/tab-login/div/div[2]/div[2]/form/div[2]/div[2]/input')
    usernsme.click()
    usernsme.send_keys(number)
    usernsme.send_keys(Keys.ENTER)
except:
    print("can't find your number bax in site")
    exit()

time.sleep(2)

try:
    taeed=driver.find_element_by_xpath('/html/body/div/app-root/app-modal-container/div/app-modal-view/div/div/div/app-confirm-custom/div/div[2]/button[2]/span')
    taeed.click()
except:
    print("can't find button taeed")
    exit()

time.sleep(2)

try:
    taeed_code=driver.find_element_by_xpath('/html/body/div/app-root/tab-login/div/div[2]/div[2]/form/div[4]/input')
    clear()
    code=input('\nplease enter your code: ')
    taeed_code.click()
    taeed_code.send_keys(code)
except:
    print("can't find your code")
    exit()

time.sleep(5)
clear()


while True:
    clear()
    try:
        time.sleep(20)
        now = jdatetime.datetime.now()
        time1=str(now.strftime("%H:%M"))
        if time1==time_sendd :
            # print("done")
            clear()
            print(now)
            print("satrt_send_massage")
            try:
                search=driver.find_element_by_xpath('/html/body/div/app-root/span/div[1]/div/rb-chats/div/div[1]/div/input')
                search.click()
                search.send_keys(names)
                search.click()
                clear()
            except:
                print("can't find search bottun") 
                exit()

            time.sleep(5)

            try:
                search1=driver.find_element_by_xpath('/html/body/div/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li/a')
                search1.click()
                clear()
            except:
                print("can't ok to search")
                exit()

            time.sleep(2)

            try:
                body=driver.find_element_by_xpath('/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[4]/div[2]')
                body.click()
                body.send_keys(massage)
                body.send_keys(Keys.ENTER)
                clear()
            except:
                print("can't find body_massage")
                exit()

            time.sleep(2)

            print("success oprate") 
            break
    except:
        print("can't run main")

driver.quit()











