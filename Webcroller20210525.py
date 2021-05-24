# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:18:39 2021

@author: dms10
"""

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)