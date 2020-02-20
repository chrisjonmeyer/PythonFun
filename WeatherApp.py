"""
    Author: Chris Meyer
    Description: Create an application that fetch the current weather
"""

import json
import socket
import re
from pprint import pprint
import requests
import geoip2.webservice

def get_my_ip():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print("My IP Address is " + ip_address)
        print("My hostname is " + host_name)
        return ip_address
    except:
        print("Unable to get IP Address")

my_ip = get_my_ip()

my_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=7abc9a643ec0a91b1e604ce98f51501c')
print (my_request.json())