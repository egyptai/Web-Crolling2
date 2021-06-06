# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:44:03 2021

@author: dms10
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import datetime

class DBUpdater:  
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root',
            password='1111', db='INVESTAR', charset='utf8')

        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code))
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date))
            """
            curs.execute(sql)
            self.conn.commit()
    
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
        sql = "select * from company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)):
            self.codes[df['code'].values.[idx]] = df['company'].values[idx]
            
        with self.conn.cursor() as curs:
            sql = "select max(last_update) from company_info"
            curs.execute(sql)
            rs =curs.fetchone()
            today = datetime.today()strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last"\
                        f"_update) values ('{code}', '{compnay}', '{today}')"
                        curs.execute(sql)
                        self.codes[code] = compnay
                        tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                        print(f"[{tmnow] #{idx+1 :0.4d} REPLACE INTO compnay_info "\
                              f"VALUES" ({code}, {compnay}, {today})")
                self.conn.commit()
                print('')
                
    def read_naver(self, code, company, pages_to_fetch):
        pass
    
    def execute_daily(self):
        self.read_krx_code()

if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()