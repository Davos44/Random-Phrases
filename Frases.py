##Getting UnicodeEncodeError: 'ascii' codec can't encode character '\xed' in position 588: ordinal not in range(128) in con.sendmail(..)

import smtplib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import random


#Scrapping data from website
my_url = '#the web address, basically a text file'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
container = page_soup.body.text[21500:-348]
splitted = container.split('. ')
no_n = [x.replace('\n','') for x in splitted]
final = []
def lenght_check():
	for element in no_n:
		if len(element) > 8:
			final.append(element)
lenght_check()


randomito = random.choices(final, k=1)
#Tried to encode it but it just sends gibberish, also tried encode.decode but to no avail
randomito_final = [x.encode('utf-8') for x in randomito]

#Sending the mail

subject = 'Subject'
body = 'Body im gonna type later"'

msg = f'Subject: {subject}\n\n{body} Tu frase motivacional de hoy es: \n {randomito}'
listing = range(0,1)
for number in listing:
	con = smtplib.SMTP('smtp.gmail.com', 587)
	con.ehlo()
	con.starttls()
	con.login('my mail', 'password')
	#I tried here with .encode,.decode, and .encode.decode but at best it just sends gibberish, at worst it doesnt work
  con.sendmail('my mail', 'other mail' , msg.encode('utf-8').decode('utf-8'))
	con.quit()
