# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:32:25 2021

@author: USUARIO
"""
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "teSTF1mCqMTam7FKaHGYXm0BsApNJITy"
url = main_api + urllib.parse.urlencode({"key":key, "front":orig, "to":dest})