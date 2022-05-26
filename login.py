# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:37:36 2022

@author: Dewo
"""
import time

username = 'whyoudewo'
password = 'rahasia'

i = 0
while i < 3:
    usr = input("Username: ")
    pas = input("Password: ")
    i += 1
    if usr == username and pas == password:
        print(f'Welcome {username}..')
        time.sleep(4)
        print("Congratulation, you're logged in.")
        break
    elif usr == username and pas != password:
        print('Password incorrect. Try again.')
        print(f'You have {3-i} more chances')
    elif usr != username and pas == password:
        print('username incorrect. Try again.')
        print(f'You have {3-i} more chances')
    else:
        print('Username & password incorrect. Try Again.')
        print(f'You have {3-i} more chances')
else:
    print('Your account blocked.')