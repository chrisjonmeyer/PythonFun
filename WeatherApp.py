"""
    Author: Chris Meyer
    Description: Create an application that fetch the current weather
"""

import json
import socket
import re

def get_my_ip():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print("My IP Address is " + ip_address)
    except:
        print("Unable to get IP Address")

get_my_ip()