import requests
from bs4 import BeautifulSoup
import csv

req = requests.get('https://www.google.com.br/')
sopa = BeautifulSoup(req.content, 'html.parser')

titulo = sopa.title
titulo_t = titulo.text

cabeça = sopa.head
cabeça_t = cabeça.text

corpo = sopa.body
corpo_t = corpo.text

img = sopa.select('img')

botão = sopa.select('input')
botões = []

for b in botão:
  valor = b.get('value')
  tipo = b.get('type') 
  classe = b.get('class')
 

  info = {
      'Tipo':tipo, 'Valor':valor, 'Classe':classe
  }
  botões.append(info)

links = []
link = sopa.select('a')
for a in link:
  href = a.get('href')
  texto = a.text
  info = {
      'Texto':texto.strip(), 'Href':href
  }
  links.append(info)

chave_botão = botões[0].keys()

with open('botões_google_scrapings.csv', 'w', newline='', encoding='utf-8') as arqv_1:
  dc = csv.DictWriter(arqv_1, chave_botão)
  dc.writeheader()
  dc.writerows(botões)
  
  chave_link = links[0].keys()

with open('links_google_scrapings.csv', 'w', newline='', encoding='utf-8') as arqv_2:
  dc = csv.DictWriter(arqv_2, chave_link)
  dc.writeheader()
  dc.writerows(links)