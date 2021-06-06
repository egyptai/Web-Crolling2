# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:16:30 2021

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
        """KRX로부터 상장기업 목록 파일을 읽어와서 데이터프레임으로 반환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'

        krx = pd.read_html(url, header=0)[0] 
        krx = krx[['종목코드', '회사명']]
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
        krx.code = krx.code.map('{:06d}'.format)
 
        print(krx)
            
    def update_comp_info(self):
        krx = self.read_krx_code()
    
    def read_naver(self, code, company, pages_to_fetch):
        pass
    
    def execute_daily(self):
        self.read_krx_code()

if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()
