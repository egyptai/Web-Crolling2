# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:15:23 2021

@author: dms10
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests


class DBUpdater:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def read_krx_code(self):
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'

        krx = pd.read_html(url, reader=0)
        print(type(krx[0]))
        print(krx[0])
        
    def read_naver(self, code, company, pages_to_fetch):
        pass
    
    def exectue_daily(self):
        self.read_krx_code()
        
if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()

