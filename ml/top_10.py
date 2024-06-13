import requests
from bs4 import BeautifulSoup
import re
def top_11(year):
    top10 = requests.get("https://www.bollywoodhungama.com/box-office-collections/worldwide/"+str(year)+"/")
    top30 = BeautifulSoup(top10.content,"html.parser")
    top301 = top30.find_all(class_='table-cell')[6:]
    name = []
    cole = []
    m = 0
    n = 1
    o = 5
    for i in top301:
        if m == n:
            x = i.text
            name.append(x[1:])
            n = n+6
        if m == o:
            y = i.text
            cole.append(float(y[1:]))
            o = o + 6
        m = m + 1
    return cole, name




# def remove_html_tags(text):
#     """Remove html tags from a string"""
#     clean = re.compile('<.*?>')
#     return re.sub(clean, '', text)
# def top_11(year):
#     top_10 = requests.get("https://en.wikipedia.org/wiki/List_of_Hindi_films_of_"+str(year))
#     top10_s = BeautifulSoup(top_10.content,"html.parser")
#     for i in range(10):
#         top10new = top10_s.find_all("tbody")[i].find_all("i")
#         top10co = top10_s.find_all("tbody")[i].find_all("span")
#         if len(top10co) != 0:
#             break
#     new10 = []
#     for i in top10new:
#         new10.append(remove_html_tags(str(i)))
#     newcole = []
#     for i in top10co:
#         newcole.append(remove_html_tags(str(i)))
    
#     newnew = []
#     y = 0
#     for i in newcole:
#         if y%2==0:
#             i = i[1:]
#             i = i[:-6]
#             newnew.append(remove_html_tags(str(i)))
#         y = y + 1
#     newnew9 = []
#     for i in newnew:
#         if len(i) >= 7:
#             i= i[:-4]
#         newnew9.append(i)
#     if len(newnew9[0]) == 0:
#         top10co = []
#         for i in range(1,31,3):
#             m = top10_s.find_all("tbody")[1].find_all("td")[i].text
#             top10co.append(m)
#         newnew10 = []
#         for i in top10co:
#             i = i[1:]
#             i = i[:-17]
#             i = i.replace("crore","")
#             i = i.replace(" ","")
#             i = i[:-1]
#             newnew10.append(float(i))
#     else:
#         newnew10 = [float(i) for i in newnew9]
#     return newnew10
