# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:08:40 2021

@author: USUARIO
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
#orig= "Quito"
#dest = "Guayaquil"
key = "teSTF1mCqMTam7FKaHGYXm0BsApNJITy"
while True:
    orig = input ("Starting location:")
    if orig =="quit" or orig== "q":
        break
    dest = input ("Destination:")
    if dest =="quit" or dest== "q":
        break
    
    url= main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("**********************************0\n")
        print("=====================================")
        print("Directions From " + (orig) + " to " + (dest))
        print("Trip Duration:  " + str(json_data["route"]["formattedTime"]))
        print("Kilometres:      "+str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel(Gal) :       "+str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("===============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61)+" Km)"))
        print("=====================\n")
    elif json_status == 402:
        print("************************")
        print("For Status Code: "+ str(json_status) + "; Invalid user inputs for one or both locations.")
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("**********************************0\n")
        print("=====================================")
    else:
        print("\n****************************************")
        print("Status Code: "+ str(json_status) + ";refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**************************************\n")
            