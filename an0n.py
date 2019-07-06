#!/usr/bin/python2
import requests
import os
import json
"""
@c0d3d by n0t3rm
#the king is back
"""
#
os.system("clear")

logo = """\033[1;32m
                  __\/__
              .  / ^  - \  .
              |\| (o)(o) |/|
       |-----.OOOo--oo--oOOO.------------------|
       |   \033[0;31mcoded by n0t3rm\033[0;0m \033[1;32m                    |
       |        \033[0;0m[\033[1;32m!\033[0;0m]\033[1;32m  An0n file uploader  \033[0;0m[\033[1;32m!\033[0;0m]\033[1;32m   |
       |   \033[1;36mtelegram\033[1;32m    : \033[0;0m@n0term\033[1;32m                |
       |        __|__                          |
       |   -------0-------                     |
       |_______________Oooo.___________________|
              .oooO    (   )
              (   )     ) /
               \ (     (_/
                \_)
\n"""

print logo
arquivo = raw_input("[\033[33m*\033[32m]\033[0;0mArquivo para upload:\33[0;0m ")

####
url = "https://anonfile.com/api/upload"
file = {'file': open(arquivo, 'rb')}
r = requests.post(url, files=file)
dict = json.loads(r.text)
#
print "\033[1;32m[\033[33m!\033[32m]\033[0;0mUpload feito com sucesso! \033[0;0m\n"
print "[\033[1;32m+\033[0;0m]url full: \033[1;37m", dict['data']['file']['url']['full']
print "[\033[1;32m+\033[0;0m]url shorten: \033[1;37m", dict['data']['file']['url']['short']
print "[\033[1;32m+\033[0;0m]id: \033[1;37m", dict['data']['file']['metadata']['id']
print "[\033[1;32m+\033[0;0m]nome do arquivo: \033[1;37m", dict['data']['file']['metadata']['name']
print "[\033[1;32m+\033[0;0m]tamanho do arquivo: \033[1;37m", dict['data']['file']['metadata']['size']['readable']
