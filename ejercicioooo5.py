# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:16:38 2021

@author: USUARIO
"""
lista1=['R1','R2','R3',"S1","S2","S3"]
switches=[]
Routers=[]
for i in lista1:
    if "S" in i:
        switches.append(i)
    if "R" in i:
        Routers.append(i)
for i in Routers:
     print(i)
for i in switches:
    print(i)
