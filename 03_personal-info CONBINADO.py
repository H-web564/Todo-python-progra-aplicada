# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:21:21 2020

@author: USUARIO
"""
nombre=input("Ingrese su nombre ")
apellido=input("Ingrese su Apellido ")
lugar=input("Ingrese lugar donde vive ")
num = int(input("Ingrese su edad "))

space=" "
print("Hola",space,nombre,apellido,space,"Vive en",lugar,"y tiene ",num,"años")
if num >= 1 and num <= 25:
    print ("y segun su edad usted es aun joven ")
elif num >=26 and num <= 62:
        print("Y segun su edad usted es un señor ")
elif num >=63 and num <= 100:
        print("Y segun su edad usted es un abuelito  ")
else:
     print("Y segun su edad usted ya fallecio XD")     
