import requests as req
from bs4 import BeautifulSoup # bs4 == Beautiful Soup, version 4
sofia = 'http://weather.bg/0index.php?koiFail=RM01opasni2&ci=14&nd=1&lng=0'
sofia = req.get(sofia)
sofia_data = sofia.content #sofia.txt is not good with encoding
sofia_html = BeautifulSoup(sofia_data, 'html.parser') #features="html5lib" got this parser from a PyCharm warning
sofia_opasni = sofia_html.body.find('div', attrs={'class': 'opasnitxt'}).getText()
sofia_tag = sofia_html.select('.gradove')
sofia_table = str(sofia_tag[0])
#
yambol = 'http://weather.bg/0index.php?koiFail=RM01opasni2&ci=2368&nd=1&lng=0'
yambol = req.get(yambol)
yambol_data = yambol.content
yambol_html = BeautifulSoup(yambol_data, 'html.parser')
yambol_opasni = yambol_html.body.find('div', attrs={'class': 'opasnitxt'}).getText()
yambol_tag = yambol_html.select('.gradove')
yambol_table = str(yambol_tag[0])
#
varna = 'http://weather.bg/0index.php?koiFail=RM01opasni2&ci=9&nd=1&lng=0'
varna = req.get(varna)
varna_data = varna.content
varna_html = BeautifulSoup(varna_data, 'html.parser')
varna_opasni = varna_html.body.find('div', attrs={'class': 'opasnitxt'}).getText()
varna_tag = varna_html.select('.gradove')
varna_table = str(varna_tag[0])
if ('Няма опасност' in sofia_table and 'Няма опасност' in yambol_table and 'Няма опасност' in varna_table):
    print('Tomorrow is going to be a calm day.')
else:
    if 'Няма опасност' in sofia_table:
        print('Sofia skipped')
    else:
        print(sofia_opasni)
    if 'Няма опасност' in yambol_table:
        print('Yambol skipped')
    else:
        print(yambol_opasni)
    if 'Няма опасност' in varna_table:
        print('Varna skipped')
    else:
        print(varna_opasni)
input()

"""
if 'Няма опасност' in sofia_table:
    print('Sofia skipped')
else:
    print(sofia_opasni)
if 'Няма опасност' in yambol_table:
    print('Yambol skipped')
else:
    print(yambol_opasni)
if 'Няма опасност' in varna_table:
    print('Varna skipped')
else:
    print(varna_opasni)
    
    
#
elif ('Няма опасност' in varna_table or 'Няма опасност' in yambol_table):
    print(sofia_opasni)
    if 'Няма опасност' in yambol_table:
        print('In Yambol tomorrow is going to be a calm day.')
        if 'Няма опасност' in varna_table:
            print('In Varna tomorrow is going to be a calm day.')
        print(varna_opasni)
    print(yambol_opasni)
    
"""