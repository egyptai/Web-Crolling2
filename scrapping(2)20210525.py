# -*- coding: utf-8 -*-
"""
Created on Tue May 25 01:59:58 2021

@author: dms10
"""
import requests

#res = requests.get("http://naver.com")
res = requests.get("http://yyy.tistory.com")

if res.status_code == requests.codes.ok:
    print("정상")
else :
    print("오류 : ", res.status_code)