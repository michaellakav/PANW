#!/usr/bin/env python
import requests
import json
import socket
import sys
sys.stdout = open('/var/www/html/atlassian-ips.html', 'w')
ip_ranges = requests.get('https://ip-ranges.atlassian.com/').json()

my_dict = ip_ranges['items']
for item in my_dict:
    print(item['cidr'])
