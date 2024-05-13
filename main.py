import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

banner = """

╔═╦═╦══╦══╦═╦╗╔══╦═╦═╦╗░
║╔╣╬║╔╗╠══╠╗║║╚╗╔╣║║║║║░
║╚╣╗╣╠╣║══╬╩╗║░║║║║║║║╚╗
╚═╩╩╩╝╚╩══╩══╝░╚╝╚═╩═╩═╝

┌─────────────────────────┐
│ Разработчик: @Fr31zep  │
└─────────────────────────┘
┌─────────────────────────┐
│[1] Поиса по номеру      │
│[2] Поиск по IP          │
│[3] DDOS                 │ 
│[4] Мануал по доксу      │
│[5] Мануал по свату      │
│[6] Мануал по сносу ТГ   │
│[7] Генератор личности   │
│[8] Генератор карты      │
│[9] Информация           │
│[10] Выйти               │
└─────────────────────────┘

"""

print(banner)

choice = input("Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python phone.py")

if choice == "2":
    os.system("clear")
    os.system("python ip.py")
    
if choice == "3":
    os.system("clear")
    os.system("python ddos.py")


if choice == "4":
    os.system("clear")
    os.system("python doks.py")

if choice == "5":
    os.system("clear")
    os.system("python swat.py")

if choice == "6":
   os.system("clear")
   os.system("python snos.py")
if choice == "7":
    os.system("clear")
    os.system("python generate.py")

if choice == "8":
    os.system("clear")
    os.system("python card.py")
    
if choice == "9":
    os.system("clear")
    os.system("python info.py")

if choice == "10":
    os.system("clear")
    os.system("python quit.py")
