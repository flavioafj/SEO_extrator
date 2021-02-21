from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pdb
import time
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import docx

wb = load_workbook(filename = 'inputs.xlsm')
sheet_ranges = wb['Planilha1']
sheet_ranges2 = wb['Planilha2']


#contar quantas linas preenchidas há na planilha
ws = wb.active
celulas_preenchidas = tuple(ws.rows)
contar = int(0)
for x in celulas_preenchidas:
    contar += 1

#vamos extrair os textos
    
document = docx.Document("Prezado.docx")
p = document.paragraphs
tamanho_txt = len(p)
y=""
for x in range(tamanho_txt):
 y += "\n" + p[x].text


coments = y.split('#$%')

#senh = input("Coloque a senha")
senh = "pconf209"

driver = webdriver.Chrome()

driver.get("https://email.uolhost.com.br/")

WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR, "input[type='password']"))

emailr = driver.find_element(By.CSS_SELECTOR, "input[type='email']")

emailr.send_keys("patioconfins@estacionamentopatioconfins.com.br")

senha = driver.find_element(By.CSS_SELECTOR, "input[type='password']")

senha.send_keys(senh)

driver.find_element(By.CSS_SELECTOR, "#login > div > form > button").click()

escrever = WebDriverWait(driver, timeout=20).until(lambda e: e.find_element(By.CSS_SELECTOR, "menu[ng-click='onComposeNew($event)']"))

try:
    escrever.click()
except:
    time.sleep(4)
    escrever.click()

iframe = WebDriverWait(driver, timeout=30).until(lambda f: f.find_element(By.CSS_SELECTOR, "iframe[aria-describedby='cke_40']"))



#email

endereco_email = driver.find_element(By.CSS_SELECTOR, "input[realfieldid='field-to']")
endereco_email.send_keys("flavioafj@yahoo.com.br")

#assunto
assunto = driver.find_element(By.CSS_SELECTOR, "input[ng-model='subject']")
assunto.send_keys("Teste2")
time.sleep(1)
assunto.send_keys(Keys.TAB + Keys.TAB)
time.sleep(1)

#texto  worContentEditable_field-body
driver.switch_to.active_element.send_keys(coments[0])


#enviar
try:
    driver.find_element(By.CSS_SELECTOR, "menu[ng-click='onSend()']").click()
except:
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "body > div.flex.flex-box-v.viewport > div > div.view-modal.webmail_accounts_folders_compose > form > div.toolbar > div.group-bt-left > menu.bt-compose-send.highlight").click()

finally:
    pdb.set_trace()

WebDriverWait(driver, timeout=10).until(EC.visibility_of(By.ID, "notifications"))







"""
driver.find_element_by_css_selector(sheet_ranges2['c2'].value).send_keys(coments[0])
driver.find_element_by_css_selector(sheet_ranges2['d2'].value).send_keys("Flávio Alves")
driver.find_element_by_css_selector(sheet_ranges2['e2'].value).send_keys("patiocontins@estacionamentopatioconfins.com.br")


for x in range(3, contar + 1):


    

    num = x - 3

    rangeb = "b{}".format(x)
    rangec = "c{}".format(x)
    ranged = "d{}".format(x)
    rangee = "e{}".format(x)
    rangef = "f{}".format(x)
    rangeg = "g{}".format(x)

    driver.implicitly_wait(10)
    b = str(sheet_ranges[rangeb].value)
    driver.execute_script("window.open('"+ b + "', '" + "new_window{}".format(num) +"')")
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(x-1))
    window_after = driver.window_handles[num + 1]
    driver.switch_to.window(window_after)

    try:
        driver.find_element_by_css_selector(sheet_ranges[rangec].value).send_keys(coments[x - 2])
    except:
        print("Não foi localizado um campo para colocar o texto em " + b )

    try:        
        driver.find_element_by_css_selector(sheet_ranges[ranged].value).send_keys("Flávio Alves")
    except:
        print("Não foi localizado um campo para colocar o nome em " + b )

    try:         
        driver.find_element_by_css_selector(sheet_ranges[rangee].value).send_keys("patiocontins@estacionamentopatioconfins.com.br")
    except:
        print("Não foi localizado um campo para colocar o e-mail em " + b )

    try:
        driver.find_element_by_css_selector(sheet_ranges[rangef].value).send_keys("https://estacionamentopatioconfins.com.br")
    except:
        print("Não foi localizado um campo para colocar url em " + b )

    try:        
        driver.find_element_by_css_selector(sheet_ranges[rangeg].value).send_keys("Título")
    except:
        print("Não foi localizado um campo para colocar o título em " + b )

    
"""



driver.close()
