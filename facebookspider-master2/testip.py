# -*- coding: utf-8 -*-
import json
import os
import urllib.request
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8123', 'https': '127.0.0.1:8123'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
print (urllib.request.urlopen('http://www.google.com'))

