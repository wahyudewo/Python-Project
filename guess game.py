# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:57:01 2022

@author: Dewo
"""

import random


def tebak(a,b):
    random_number = random.randint(a, b)
    
    guess = 0
    while guess != random_number:
        guess = int(input(f'Tebak angka dari {a} sampai {b}: '))
        if guess < random_number:
            print('Tebak lagi, terlalu rendah.')
        elif guess > random_number:
            print('Tebak lagi, kelebihan.')
        
    print(f'Yeyy kamu benar! angkanya adalah {random_number}')

def tebak_1(a,b):
    feedback = ''
    while feedback != 'b':
        if a != b:
            guess = random.randint(a, b)
        else:
            guess = b
        feedback = input(f'Apakah benar angkanya {guess}? Lebih (l), Kurang (k), Benar (b): ').lower()
        if feedback == 'l':
            b = guess - 1
        elif feedback == 'k':
            a = guess + 1
    
    print(f'Yeyy komputer berhasi menebak angkamu, {guess}, dengan benar')

tebak_1(a = int(input('Masukkan rentang bawah: ')), b = int(input('Masukkan rentang atas: ')))
