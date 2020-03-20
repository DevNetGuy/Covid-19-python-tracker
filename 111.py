#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2

def main():
    print("(1) view all Cases in the World ")
    print("(2) view cases for a Specific Country")

    choice = raw_input('\nEnter your Choice> ')
    view(choice)
   
def view(ch):
    if(ch == "1"):
        req = urllib2.Request('https://corona-stats.online/?format=json')

    elif(ch == "2"):
        countryName = raw_input('Enter Country Name:')
        req = urllib2.Request('https://corona-stats.online/'+str(countryName)+'?format=json')
    else:
        exit()

    response = urllib2.urlopen(req)
    the_page = response.read()

    try:
        obj = json.loads(the_page)
        for i in obj:
            print("------------")
            print("Country: " + str(i['country']))
            print("province: " + str(i['province']))
            print("Confirmed: " + str(i['confirmed']))
            print("Recovered: " + str(i['recovered']))
            print("Active: " + str(i['active']))
            print("Deaths: " + str(i['deaths']) + " 😞")
            print("------------")
    except ValueError:
            print("\n[-] Country not Found\n")
            main()

print("[!] COVID-19 Cases Tracker.")
print("By: Abadee M.Alwerfali")
print("Stay Safe by staying Home 🙏")
print("")

main()


