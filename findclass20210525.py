# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:50:57 2021

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
        </ul>
        <ul class = "reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul", {"class":"reply"})
print(ul)
