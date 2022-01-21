#!/usr/bin/env python
import requests
import json
import socket
import sys
sys.stdout = open('/var/www/html/azure-ips.html', 'w')
ip_ranges = requests.get('https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20220117.json').json()
my_dict = ip_ranges['values']

for item in my_dict:
     print((json.dumps(item['properties']['addressPrefixes']) +"\n" ).replace('"', '').replace('[', '').replace(']', '').replace(',', '\n'))