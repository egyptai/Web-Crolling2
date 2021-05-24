# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:41:16 2021

@author: dms10
"""

import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        <ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
#print(ul)
#li = ul.find("li")
lis = ul.findAll("li")
#print(li.text)
print(lis)
print(lis[1].text)