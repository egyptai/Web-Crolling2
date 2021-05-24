# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:05:00 2021

@author: dms10
"""

from urllib.request import urlopen

url = "https://www.naver.com"
html = urlopen(url)
print(html.read())