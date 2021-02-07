# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:04:47 2020

@author: USUARIO
"""
aclNum = int(input("What is the IPv4 ACL numbre? "))
if aclNum >= 1 and aclNum <= 99:
    print ("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
        print("This is a extended IPv4 ACL.")
else:
     print("This is not a standard or extended IPv4 ACL")        