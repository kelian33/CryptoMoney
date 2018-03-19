#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import requests

liste_nom=requests.get('https://www.cryptocompare.com/api/data/coinlist/')
datas=liste_nom.json()
names_money = datas['Data']
fini = False

while fini != True :
    money = input("Entrez le nom d'une cryptomoney sinon tapez 'liste' ou 'exit' : ")

    if(money == "liste"):
        for name_money in names_money :
	        print(name_money)
        fini = False

    elif(money == "exit"):
        fini = True

    else :	    
        liste_prix = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+money+'&tsyms=USD,EUR')
        prix=liste_prix.json()

        print("1",money,"=",prix['EUR'],"€")
        print("1",money,"=",prix['USD'],"$")
        fini = False
