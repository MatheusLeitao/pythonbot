import time
import loading
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:\wamp64\www\python\webdriver\chromedriver.exe")
driver.set_page_load_timeout(10)

def getid(list):
    for mec in list:
        id = mec.get_attribute('id')
        return id

def qtdtags():
    datas = []
    counter = 0
    tagsqtd = 0
    with open('C:/wamp64/www/python/noems.txt', 'r') as file:
        time.sleep(1)
        linesfromfile = file.readlines()
        for tags in linesfromfile:
            datas = tags.split()
            dataslength = len(datas)
            while counter < dataslength:
                if counter != 0:
                    tagsqtd += 1
                counter += 1
            counter = 0
    return tagsqtd

def addpass():
    with open ('C:/wamp64/www/python/login.txt', 'w+') as login:



with open('C:/wamp64/www/python/noems.txt', 'r') as file:
    fileslines = file.readlines()
    deleteline = len(fileslines) - 1
    perfil = fileslines[deleteline]

with open('C:/wamp64/www/python/noems.txt','w') as newfiles:
    for pos, lines in enumerate(fileslines):
        if pos is not deleteline:
            newfiles.write(lines)


time.sleep(1)

qtd_tag = qtdtags()


os.system('cls')

print("\n")
print(f"*** NO CONDOMINIO EXISTEM {deleteline} APARTAMENTOS E {qtd_tag} TAGS PARA SEREM ADICIONADOS *** ")
print(F"***PERFIL A SER ADICIONADO {perfil} DO CONDOMINIO {perfil[6:19]}***")
print("\n")
print("\n")

os.system('pause')



data = []
x = 0
z = 0

os.system('cls')


localweb = 'http://localhost:8080'
user = "admin"
password = "tattica123web"

print(f"LOGANDO NO SITE {localweb}")
with open('C:/wamp64/www/python/noems.txt', 'r') as files:
    filesline = files.readlines()

driver.get(localweb)
time.sleep(1)
print(f"USUARIO: {user}")
userpath = driver.find_element_by_name('user')
print(f"SENHA: {password}")
passwordpath = driver.find_element_by_name('password')
userpath.send_keys(user)
passwordpath.send_keys(password)
passwordpath.send_keys(Keys.ENTER)
print("ADICIONANDO NOVO CADASTRO")
time.sleep(1)
driver.find_element_by_id('tbr_mnu_usuarios_toolbar-btnEl').click()#Clicar no menu de usuarios

for tags in filesline:
    data = tags.split() # SEPARAÇAO DE COLUNAS DE TODAS AS LINHAS
    tamanho = len(data) # PEGA O TAMANHO DO VETOR
    os.system('cls')
    print(f"ADICIONANDO APT {data[0]} NO PERFIL {perfil}")
    time.sleep(2)
    while x < tamanho:
        if x == 0:
            time.sleep(0.5)
            addbutton_id = getid(driver.find_elements_by_xpath('//*[starts-with(@id, "toolbarcadastro-") and contains(@id, "tlbLocalizarNovo-btnEl")]'))#Clicar em adicionar novo usuario
            driver.find_element_by_id(addbutton_id).click()
            driver.find_element_by_name("nome").send_keys(data[0])#Adicionar o nome do usuario
            time.sleep(1)
            driver.find_element_by_xpath("//*[contains(text(), 'Perfis')]").click()#Clicar na aba de perfis
            driver.find_element_by_id('pnlCadastroUsuarioPerfil_txtPerfil_btnSearchField-btnEl').click()#Clicar lupa para escolher perfil
            time.sleep(0.5)
            # driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div[2]/div[3]/div/fieldset/div/div[1]/div[1]/em/button').click()#Buscar novo perfil
            driver.find_element_by_id('pnlLocalizar_txtConsultar-inputEl').send_keys(perfil)#Perfil de acesso
            print(f"ADICIONADO {data[0]} NO PERFIL {perfil}")
            time.sleep(1)          
            driver.find_element_by_xpath('/html/body/div[11]/div[2]/div[1]/div/div[1]/div[2]/div/table/tbody/tr[2]/td').click()#Clica para escolher perfil
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[3]/div/fieldset/div/div[2]/em/button').click()#Adiciona perfil
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[4]/em/button').click()#Aba cartões adicionais
        else:
            nometag = "TAG 0" + str(x)
            print(f"ADICIONANDO {nometag} - CODIGO: {data[x]} ")
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[4]/div/fieldset/div/table[1]/tbody/tr/td/input').send_keys(nometag)#NOME DO TAG
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[4]/div/fieldset/div/div[1]/table[3]/tbody/tr/td/input').send_keys(data[x])# TAG A SER ADICONADO
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[4]/div/fieldset/div/div[2]/em/button').click()#ADICIONAR O TAG
            qtd_tag -= 1
            pass

        x += 1
        pass
    
    if x == tamanho:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[3]/em/button').click()# CLICAR EM SALVAR QUANDO TERMINAR
        time.sleep(0.5)
        if z == 0:
            okid = ""
            time.sleep(4)
            driver.find_element_by_xpath('//*[contains(text(), "OK")]').click()#Clicar em OK quando salva
            okid = driver.find_element_by_xpath('//*[contains(text(), "OK")]').get_attribute('xpath')
        else:
            deleteElement = driver.find_element_by_xpath('//*[contains(text(), "OK")]').get_attribute('id')
            deleteElId = deleteElement[7:11]
            js = "aa =document.getElementById('button-"+ deleteElId +"'); aa.remove()"
            driver.execute_script(js)
            time.sleep(2)
            nextId = driver.find_element_by_xpath('//*[contains(text(), "OK")]').get_attribute('id')
            newElement = "button-"+ nextId[7:11] +"-btnEl"
            driver.find_element_by_id(newElement).click()
            pass
        print("ADICIONANDO NOVO APARTAMENTO...")
        time.sleep(0.9)
        driver.find_element_by_id('tbr_mnu_usuarios_toolbar-btnEl').click()#Clicar em adicionar novo usuario

        x = 0
        z += 1
        pass
    pass

# C:\Users\MATHEUS-PC\AppData\Local\Programs\Python\Python38\python.exe -i C:/wamp64/www/python/cadastrotag_bot.py