# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:53:14 2021

@author: USUARIO
"""

file=open('devices.txt',"a")
while True:
    newItem=input("Ingrese un nuevo intem: ")
    if newItem== "Exit":
        print('Acceso concedido')
        break
    else:
        file.write(newItem+ "\n")
file.close()
