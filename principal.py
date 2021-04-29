from selenium import webdriver
import pyautogui
from time import sleep

#ler dados da pessoa
nome = str(input('Digite seu nome: '))
nome_user = str(input('Digite o nome do usuario: '))
email = str(input('Digite seu email: '))
senha = str(input('Digite a senha: '))

navegador = webdriver.Chrome(executable_path=r'chromedriver.exe') # localizar o arquivo .exe do selenium
navegador.get('https://www.instagram.com/accounts/emailsignup/')
sleep(1)
navegador.find_element_by_css_selector('._2hvTZ.pexuQ.zyHYP').click()
pyautogui.write(email)
sleep(1)
navegador.find_element_by_name('fullName').click()
pyautogui.write(nome)
sleep(1)
navegador.find_element_by_name('username').click()
pyautogui.write(nome_user)
sleep(1)
navegador.find_element_by_name('password').click()
pyautogui.write(senha)
sleep(1)
pyautogui.moveTo(527, 598) # necessario talvez fazer mudaças dependendo do tamanho do seu monitor
sleep(1)
pyautogui.click()