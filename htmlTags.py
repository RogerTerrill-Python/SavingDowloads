#!/usr/bin/env python3

import os, bs4, requests

newFile = open('AntairaList.html', 'wb')

antaira = requests.get('http://www.antaira.com/s.nl?ext=F&sc=46&category=&search=lnx')
antaira.raise_for_status()

antairaObj = bs4.BeautifulSoup(antaira.text)

antairaTitle = antairaObj.select('.relatedItemTitle')

for titles in antairaTitle:
    titlesText = titles.getText() + "<br />"    #if you add "\n" it only adds that to text, you have to use <br /> for html
    newFile.write(titlesText.encode('utf-8'))
    
newFile.close()