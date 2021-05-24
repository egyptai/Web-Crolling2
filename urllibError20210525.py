# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:14:16 2021

@author: dms10
"""

from urllib.request import urlopen
from urllib.request import HTTPError

try:
    html = urlopen("http://www.google.com/kim.html")
except HTTPError as e:
    print(e)
else:
    print("성공")