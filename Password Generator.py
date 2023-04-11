#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?'

password = ''
for c in range(10):
    password = random.choice(chars)
password += random.choice(chars)

length = input('password length?')
length = int(length)

password = ''
for c in range(length):
    password += random.choice(chars)
    print(password)