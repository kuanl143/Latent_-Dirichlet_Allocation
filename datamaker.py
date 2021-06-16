# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:38:46 2021

@author: KUNAL
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


data = []
print("Process started!")
for i in range(200):
    # url of arXiv web page
    url = "https://arxiv.org/search/?query=cs.LG&searchtype=all&order=-announced_date_first&size=50&abstracts=show&start="

    # get html content
    r = requests.get(url + str(i)) # range(200)
    html_content = r.content

    soup = BeautifulSoup(html_content,'html.parser')


    spans = soup.find_all('span',class_ = 'abstract-full has-text-grey-dark mathjax')
    titles = soup.find_all('p',class_ = "title is-5 mathjax")

    for j in range(50):
        data.append([titles[j].get_text().split('\n')[2].strip(),spans[j].get_text().split('\n')[1].strip()])

    print(f"{i}th web page done!")
            
df_ = pd.DataFrame(data,columns=['Title','Abstract'])
df_.to_csv("Data.csv")