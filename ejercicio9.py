# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:13:26 2021

@author: USUARIO
"""

acl=int(input('Ingrese la # de ACL'))
if acl >=1 and acl <=99:
    print('La ACL es Estandar')
elif acl >=100 and acl <=199:
    print('La ACL es Extendida')
else:
    print('El # ingresado no es una ACL ')