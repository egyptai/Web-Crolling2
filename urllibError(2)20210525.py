# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:16:28 2021

@author: dms10
"""

from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    html = urlopen("http://www.dddsdf.com/kim.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found! ')
else:
    print("성공")