# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:34:51 2021

@author: dms10
"""

import bs4

html_str = "<html><div>hello</div></html>"
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))