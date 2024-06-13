import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def coment_analis(movoie_input):
    seach_movie = "https://www.google.com/search?q="
    seach_movie1 ="&rlz=1C1RXQR_enIN930IN930&biw=1280&bih=601&sxsrf=AJOqlzVNqE_3ckZuDArKrajullgip_qHlQ%3A1678611194327&ei=-pINZMPKE8aL4-EPt6udiAY&ved=0ahUKEwjDr9D_gdb9AhXGxTgGHbdVB2EQ4dUDCA8&uact=5&oq="
    seach_movie2 = "&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIFCAAQgAQyBggAEBYQHjIFCAAQhgM6CggAEB4QogQQsAM6CAgAEKIEELADSgQIQRgBUJ4GWNAKYMAQaAFwAHgAgAGiAYgB-ASSAQMwLjSYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp"
    # movie_site = requests.get(seach_movie+seach_input+" movie collction sacnilk.com&num=1&gl=india")
    # movie_request = requests.get("https://www.google.com/search?q="+ movoie_input +" review imdb&num=1&gl=india")
    # movie_request = requests.get(seach_movie+movoie_input+" review imdb&num=1"+seach_movie1+movoie_input+" review imdb"+seach_movie2)
    movie_request = requests.get(seach_movie+"imdb "+movoie_input+"&num=1"+seach_movie1+"imdb "+movoie_input+seach_movie2)
    coment_request = BeautifulSoup(movie_request.content,"html.parser")
    coment_request1 = coment_request.find(class_="BNeawe s3v9rd AP7Wnd")('a')[0].get('href')
    coment_request1 = coment_request1[7:-87]
    coment_request2 = requests.get(coment_request1)
    coment_request3 = BeautifulSoup(coment_request2.content,'html.parser')
    # coment_request4 = coment_request3.find_all(class_='text')
    coment_request4= []
    for i in range(25):
        coment_request4.append(coment_request3.find_all(class_='text')[i].text)
    new = pd.DataFrame(coment_request4)
    sentiments = SentimentIntensityAnalyzer()
    com_sen = []
    for i in range(len(new)):
        sen1 = sentiments.polarity_scores(new[0][i])
        if sen1['compound'] >= 0.5:
            com_sen.append(1)
        else:
            com_sen.append(0)
        # com_sen.append(sen1['compound'])
    return new, com_sen
