import os
import requests
import time
print("""
 ▄▀▀█▄▄   ▄▀▀█▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄   
█ ▄▀   █ ▐ ▄▀   █ █   █   █ ▐  ▄▀   ▐ █      █  
▐ █    █   █▄▄▄▀  ▐  █▀▀█▀    █▄▄▄▄▄  █      █  
  █    █   █   █   ▄▀    █    █    ▌   ▀▄▄▄▄▀▄  
 ▄▀▄▄▄▄▀  ▄▀▄▄▄▀  █     █    ▄▀▄▄▄▄           █ 
█     ▐  █    ▐   ▐     ▐    █    ▐           ▐ 
▐        ▐                   ▐                  
""")
print("OPTIONS")
print("'GET' (Only Show The DB)")
print("'POST' (Add A Value In The DB)")
print("'DELETE' (Delet A Value In DB)")
escolha1 = input("Option:  ").upper()

if escolha1 == "GET":
    url = input("Type A URL: ")
    req = requests.get(url)
    print(req)
    time.sleep(1)
    print(req.json())
    time.sleep(3)

elif escolha1 == "POST":
    url = input("Type A URL: ")
    infor = input("Type A Value (exemple: {'banana': 'abacate'}): ")
    req = requests.post(url, data=infor)
    time.sleep(1)
    print("successful!")

elif escolha1 =="DELETE":
    url = input("Type A URL: ")
    requests.delete(url)
    print("succesfull!")
