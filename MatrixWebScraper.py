import time
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from datetime import date 
from datetime import timedelta


today = datetime.today() - timedelta(days=25)
d1 = today.strftime("%Y%m%d") 
final = str(d1) + '+'


driver = webdriver.Chrome('/Users/louisvranderick/chromedriver')  # Optional argument, if not specified will search path.
link = 'https://matrix.centris.ca/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ5Nzk0DUAGAwAAAAfDv8K6woFLDQIL&f='
driver.get(link);
wait = WebDriverWait(driver, 10)

def login(user, password):
    #declaration de variable
    #chaque bouton ou action avec selenium a sa propre variable
    userCode = driver.find_element(By.ID, "UserCode")
    passWord = driver.find_element(By.ID, "Password")  
    button = driver.find_element(By.XPATH, "/html/body/div/main/div/div[2]/div[1]/div/div/form/button")
    #Login page
    userCode.send_keys(user)
    passWord.send_keys(password)
    button.click()  


    substring = "LoginIntermediate"

    if substring in driver.current_url:
        interButton = driver.find_element(By.ID, "btnContinue")
        interButton.click()
    else: 
        pass

#region doit pas avoir d'erreur: Montréal, Laval
def criteres(region, sousRegion, prix):
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/ul/li[1]/a")))
    #main page actions
    recherche = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/ul/li[1]/a")
    recherche.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[6]/div/div[2]/span/span[1]/div/table/tbody/tr/td/table[2]/tbody/tr/td/a[1]")))
    #second search page actions 
    general = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/div/div[2]/span/span[1]/div/table/tbody/tr/td/table[2]/tbody/tr/td/a[1]")
    general.click() 


    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]/a")))
    #Critères 
    More = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[2]/div/div/div[1]/div[1]/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[1]/table/tbody/tr/td[1]/select/option[6]")
    Statut = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[2]/div/div/div[1]/div[1]/div/table/tbody/tr[1]/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/select/option[2]") 
    Nonexpire = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[2]/div/div/div[1]/div[1]/div/table/tbody/tr[1]/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/select/option[1]")  
    Vendre = driver.find_element(By.ID, "Fm43_Ctrl3386_TB")
    date = driver.find_element(By.ID, "Fm43_Ctrl3416_TB")
    button = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[5]/a")

    #send in
    More.click()
    if sousRegion == 0 : 
        driver.find_element(By.XPATH, "//*[@title='"+region+"']").click()
    else:
        driver.find_element(By.XPATH, "//*[@title='"+region+"']").click()
        driver.find_element(By.XPATH, "//*[@title='"+sousRegion+"']").click()
    #DeRégion.click()
    Statut.click()
    Nonexpire.click()
    date.send_keys(final) 
    Vendre.send_keys(prix)
    button.click()





def processpropertys():
    #open first property
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span/b[2]")))
    #ouvrir la premiere propriété 
    number = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span/b[2]").text 
    first = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div/select")
    first.click()
    driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div/select/option[3]").click()

    for i in range(int(number)): 
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td/span")))
        Adresse = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr[2]/td/span").text
        Adresse2 = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr[3]/td/span").text
        button = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span/span/a[2]")
        Price = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/span").text
        numCentris = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/b/span").text
        zip = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/span").text 
        driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[3]/div[3]/div/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/span/div/table/tbody/tr/td/table/tbody/tr[1]/td[3]/span/div/table/tbody/tr/td/table/tbody/tr/td[1]/span/a").click()
        driver.switch_to.window(driver.window_handles[1])
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr[1]/td/div/div/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[8]/td/table/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/span")))

        proprio = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td/div/div/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[8]/td/table/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[1]/td[1]/span").text
        AdresseProprio = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td/div/div/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[8]/td/table/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[1]/span").text
        AdresseProprio2 = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td/div/div/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[8]/td/table/tbody/tr[3]/td/span/div/table/tbody/tr/td/table/tbody/tr[3]/td[1]/span").text
        driver.switch_to.window(driver.window_handles[0])
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[6]/table/tbody/tr/td/div[2]/div[1]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span/span/a[2]"))) 
        button.click()
        url = "https://api.followupboss.com/v1/events"
        
        payload = {
            "person": {
                "contacted": False,
                "tags": [ 
                    Adresse2
                ],
                "addresses": {"n": {
                    "street": Adresse,
                    "city": Adresse2,
                    "code": zip
                    }},
                "firstName": proprio,
                "stage": "Lead"
            },
            "source": "Expiré - Unifamiliale - Wassim",
            "system": "Matrix.ca",
            "type": "Registration",
            "message": "Nouvelle propriété expiré, numéro centris " + numCentris +  "\n Adresse du proprio: " + AdresseProprio + " " + AdresseProprio2 
            + "\n Prix de le propriété expiré: " + Price
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Basic ZmthXzBHSjd6elNyN1JxRHNDcHIySDdzbU1CMmgyTThDNk5PWlM6"
        }
        response = requests.post(url, json=payload, headers=headers)

login('', '') #login du courtier
criteres('Montréal','Mont-Royal','1+')
processpropertys()
criteres('Montréal','Montréal (Saint-Laurent)','1+')
processpropertys()
criteres('Montréal','Montréal (Outremont)','1+')
processpropertys() 
criteres('Montréal','Montréal (Ahuntsic-Cartierville)','1+')
processpropertys()


time.sleep(5) 

driver.quit()
