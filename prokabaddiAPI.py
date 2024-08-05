from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import socket

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

def isOnline():
    return socket.gethostbyname(socket.gethostname()) !="127.0.0.1"

def get_all_team_url():
    if isOnline:
        driver.get("https://www.prokabaddi.com/stats")
        g= [i.replace("/players","") for i in [i.get_attribute('href') for i in driver.find_elements(By.TAG_NAME, 'a') if i != None] if i != None if "players" in i]
        return [{"TeamName":' '.join(i.split('/')[-1].split('-')[:-2]).replace('-', ' ').title(),"TeamURL":i} for i in g]
    else:
        raise Exception('No internet')

def get_all_player_url():
    if isOnline:
        teams = get_all_team_url()
        players=[]
        for i in teams:
            driver.get(i["TeamURL"])
            sleep(1)
            r4=driver.find_elements(By.CLASS_NAME,"squad-name")
            r5=driver.find_elements(By.CLASS_NAME,"squad-category")
            r6=driver.find_elements(By.CLASS_NAME,"btn-more")
            for i in range(0,len(r4)):
                players.append({"name":r4[i].get_attribute("innerText").replace("\n"," "),"category":r5[i].get_attribute("innerText"),"profileURL":r6[i].get_attribute("href")})
        return players
    else:
        raise Exception('No internet')

def get_team_stats_from_url(url):
    if isOnline:
        driver.get(url)
        main_arr=[]
        sleep(2)
        seasons=driver.find_elements(By.CLASS_NAME,"list-item")
        for x in range(0,len(seasons)):
            driver.execute_script("document.getElementsByClassName('list-item')["+str(x)+"].click();")
            driver.execute_script("document.getElementsByClassName('list-item')["+str(x)+"].click();")
            sleep(1)
            arr=[]
            players=[]
            arr.append({"season":driver.find_elements(By.CLASS_NAME,"title")[5].get_attribute("innerText")})
            r0=driver.find_elements(By.CLASS_NAME,"information-label")
            r1=driver.find_elements(By.CLASS_NAME,"information-count")
            r2=driver.find_elements(By.CLASS_NAME,"graph-label")
            r3=driver.find_elements(By.CLASS_NAME,"graph-value")
            r4=driver.find_elements(By.CLASS_NAME,"squad-name")
            r5=driver.find_elements(By.CLASS_NAME,"squad-category")
            r6=driver.find_elements(By.CLASS_NAME,"btn-more")
            for i in range(0,len(r0)):
                arr.append({r0[i].get_attribute("innerText"):r1[i].get_attribute("innerText")})
            for i in range(0,len(r2)):
                arr.append({r2[i].get_attribute("innerText"):r3[i].get_attribute("innerText")})
            for i in range(0,len(r4)):
                players.append({"name":r4[i].get_attribute("innerText").replace("\n"," "),"category":r5[i].get_attribute("innerText"),"profileURL":r6[i].get_attribute("href")})
            arr.append({"players":players})
            main_arr.append(arr)
        return main_arr
    else:
        raise Exception('No internet')

def get_player_stats_from_url(url):
    if isOnline:
        driver.get(url)
        main_arr=[]
        main_arr.append({"teamName":driver.find_elements(By.CLASS_NAME,"name-section")[0].get_attribute("innerText").replace("\n"," ")})
        driver.find_elements(By.CLASS_NAME,"tab-name")[1].click()
        seasons=driver.find_elements(By.CLASS_NAME,"list-item")
        for x in range(0,len(seasons)):
            driver.execute_script("document.getElementsByClassName('list-item')["+str(x)+"].click();")
            driver.execute_script("document.getElementsByClassName('list-item')["+str(x)+"].click();")
            sleep(0.5)
            arr=[]
            arr.append({"season":driver.find_elements(By.CLASS_NAME,"title")[2].get_attribute("innerText")})
            r0=driver.find_elements(By.CLASS_NAME,"information-label")
            r1=driver.find_elements(By.CLASS_NAME,"information-count")
            r2=driver.find_elements(By.CLASS_NAME,"graph-label")
            r3=driver.find_elements(By.CLASS_NAME,"graph-value")
            for i in range(0,len(r0)):
                arr.append({r0[i].get_attribute("innerText"):r1[i].get_attribute("innerText")})
            for i in range(0,len(r2)):
                arr.append({r2[i].get_attribute("innerText"):r3[i].get_attribute("innerText")})
            main_arr.append(arr)
        return main_arr
    else:
        raise Exception('No internet')