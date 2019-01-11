#-*-coding:utf8;-*-
#qpy:3
#qpy:console
A='\033[1;31m'
B='\033[1;32m'
C='\033[1;33m'
D='\033[1;34m'
E='\033[1;35m'
F='\033[1;36m'

import os
a='Goodlist.py'
b='goodlist'
os.system('mv {} /data/data/com.termux/files/usr/bin/'.format(a))
c="alias {}='python /data/data/com.termux/files/usr/bin/{} ' ". format(b, a)
file=open('/data/data/com.termux/files/usr/etc/bash.bashrc','r')
comundes=file.readlines()
if c in comundes :
    print(D,'Sorry !!',B,'{} is found !! '.format(b))
else :
    file=open('/data/data/com.termux/files/usr/etc/bash.bashrc','a')
    file.write('\n')
    file.write(c)
    file.close()
    file=open('/data/data/com.termux/files/usr/etc/fish/config.fish','a' )
    file.write('\n')
    file.write(c)
    file.close()
    print(B,'[OK]',C," + Saved")
