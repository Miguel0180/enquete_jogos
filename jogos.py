# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pyautogui as pa
import time
import pyscreeze
import keyboard


pa.PAUSE = 1


Clubes = ['Botafogo', 'Flamengo', 'Palmeiras', 'Bahia', 'Athletico-PR', 'Cuiabá', 'Criciúma', 'Juventude', 'Vitória', 'Cruzeiro', 'Red Bull Bragantino',
          'Fluminense', 'Atlético-GO', 'Vasco', 'Corinthians', ' Atlético-MG', 'Grêmio', 'São Paulo', 'Fortaleza', 'Internacional']

link = "https://www.flashscore.com.br/futebol/brasil/brasileirao-betano/calendario/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, "html.parser")

print(requisicao)


'''

try:
    rodada = site.findAll("span")
    for n in range(20):
        print(rodada[n])
        print('')

except:
    print('acabou')


print(rodada[6])
'''

#ws = Whatsap enquete / sl = show list /  rm = remover item da lista / re = reset da lista 


print('')
#Span do site que contem a parte dos jogos
rodada = site.find("span", class_="next_round").text

#Padrão para remover data
pattern = r'(\d{2}/\d{2}):'

#Exclui as datas da string
matches = re.sub(pattern, '', rodada).strip()

#Forma uma lista dividindo cada item pela vírgula
jogos = matches.split(',')
print(jogos)

#Separa cada jogo em uma lista e cada time em uma tupla
lista_tuplas = [tuple(jogo.split(' x ')) for jogo in jogos]
print(lista_tuplas)

print(lista_tuplas[1][1])



def iniciar():
    pa.press('win')
    pa.write("chrome")
    pa.press('ENTER')
    pa.write("https://web.whatsapp.com/")
    pa.press('ENTER')
    time.sleep(8)

iniciar()


pa.click(x=178, y=178)
pa.write('Pro clubs')
pa.click(x=252, y=346)

for i in range (10):
    try:
        mais = pyscreeze.locateCenterOnScreen('imagens/mais.png')
        print(mais)
        pa.click(mais)
        enquete = pyscreeze.locateCenterOnScreen('imagens/enquete.png')
        pa.click(enquete)
    except:
        pa.click(x=556, y=696)
        pa.click(x=580, y=552)
    keyboard.write('Qual será o resultado?')
    pa.click(x=587, y=407)
    keyboard.write(lista_tuplas[i][0])
    pa.click(x=569, y=494)
    pa.write('Empate')
    pa.click(x=569, y=510)
    keyboard.write(lista_tuplas[i][1])
    pa.click(x=864, y=585)
    try:
        enviar = pyscreeze.locateCenterOnScreen('imagens/enviar.png')
        pa.click(enviar)
    except:
        pa.click(x=853, y=662)
