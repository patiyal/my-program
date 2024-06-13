import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
def top_100_movie(hello):
    top100 = requests.get('https://www.sacnilk.com/entertainmenttopbar/Top_500_Bollywood_Movies_Of_All_Time')
    top100soup = BeautifulSoup(top100.content,"html.parser")
    top100soup1 = top100soup.find(class_='table')
    top100soup2 = top100soup1.find_all('tr')[1:]
    movie_name = []
    worldwidecollection = []
    india_collection = []
    budget = []
    verdict = []
    y = 0
    for i in top100soup2:
        movie_name.append(i.find_all('td')[1].text)
        worldwidecollection.append(i.find_all('td')[2].text)
        india_collection.append(i.find_all('td')[4].text)
        budget.append(i.find_all('td')[6].text)
        verdict.append(i.find_all('td')[7].text)
    wc = []
    for i in worldwidecollection[:50]:
        wc.append(float(i))
    ic = []
    for i in india_collection[:50]:
        ic.append(float(i))
    bg = []
    for i in budget[:50]:
        bg.append(float(i))
    mo_co = pd.DataFrame(zip(wc,ic,movie_name,bg,verdict), columns=['World Collection', 'India Collection','Movie Name','Budget','Verdict'])
    mo_co = mo_co.sort_values(by='World Collection',ascending=False, ignore_index=True)
    return mo_co