# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:02:20 2021

@author: dms10
"""
import requests
res = requests.get("http://naver.com")

res.raise_for_status()
print("정상입니다.")
print(len(res.text))
print(res.text)