from bs4 import BeautifulSoup
import requests
import plotly.express as px
def all_day(movie_nam):
    movie_nam = movie_nam.lower()
    movie_nam = movie_nam.replace(" ","-")
    day_by_day = requests.get('https://www.bollywoodhungama.com/movie/'+movie_nam+'/box-office/#bh-movie-box-office')
    movie_day_co = BeautifulSoup(day_by_day.content,"html.parser")
    movi11 = movie_day_co.find_all(class_ = 'tablesaw tablesaw-swipe')[2]
    movi12 = movi11.find_all('td')
    day = []
    coleee = []
    mm = 0
    nn = 2
    xx = 0
    for i in movi12:
        if xx == mm:
            day.append(i.text)
            mm = mm + 4
        if xx == nn:
            ii = i.text
            ii = ii[1:-4]
            coleee.append(float(ii))
            nn = nn + 4
        xx = xx + 1
    collq = movie_day_co.find_all(class_ = 'tablesaw tablesaw-swipe')[8]
    # try:
    #     y = 0
    #     for i in (collq.find_all('td')[3:])[::2]:
    #         if y == 0:
    #             m = i.text
    #             india_coll12 = float(m[1:-3])
    #         if y == 1:
    #             m = i.text
    #             budget12 = float(m[1:-3])
    #         if y == 2:
    #             m = i.text
    #             world_coll12 = float(m[1:-3])
    #         y = y + 1
    # except:
    seach_movie = "https://www.google.com/search?q="
    seach_movie1 ="&rlz=1C1RXQR_enIN930IN930&biw=1280&bih=601&sxsrf=AJOqlzVNqE_3ckZuDArKrajullgip_qHlQ%3A1678611194327&ei=-pINZMPKE8aL4-EPt6udiAY&ved=0ahUKEwjDr9D_gdb9AhXGxTgGHbdVB2EQ4dUDCA8&uact=5&oq="
    seach_movie2 = "&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIFCAAQgAQyBggAEBYQHjIFCAAQhgM6CggAEB4QogQQsAM6CAgAEKIEELADSgQIQRgBUJ4GWNAKYMAQaAFwAHgAgAGiAYgB-ASSAQMwLjSYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp"
    movie_site = requests.get(seach_movie+movie_nam+" movie collction sacnilk&num=1"+seach_movie1+movie_nam+" movie collction sacnilk"+seach_movie2)
    soup = BeautifulSoup(movie_site.content ,"html.parser")
    fidn = soup.find(class_="egMi0 kCrYT")
    fidn = fidn.find('a')
    fidn = fidn.get('href')
    fidn = fidn[7:]
    fidn = fidn[:-96]

    # movie_site = requests.get(seach_movie+seach_input+" movie collction sacnilk.com&num=1&gl=india")
    rrrrr = requests.get(fidn)
    rrrr = BeautifulSoup(rrrrr.content,"html.parser")
    rs = rrrr.find(class_ = 'newscontenthighlight')
    # rss = rs.find_all_next()
    dfg = rs.find_all_next(text= True)
    yy = 0
    india = ""
    worlcolle =""
    buged =""
    verdi = ""
    for i in dfg:
        if yy == 3:
            worlcolle = i.text
            worlcolle = worlcolle[23:-3]
        if yy == 9:
            india = i.text
            india = india[25:-3]
        if yy == 12:
            buged = i.text
            buged = buged[18:-3]
        if yy == 14:
            if len(''.join(filter(str.isdigit, i))) <= 0:
                verdi = i.text
            else:
                verdi = ''
        if len(india) == 0:
            if yy == 14:
                india = i.text
                india = india[25:-3]
        if len(buged) == 0:
            if yy == 17:
                buged = i.text
                buged = ''.join(filter(str.isdigit, buged))
        if len(verdi) == 0:
            if yy == 24:
                verdi = i.text
        yy = yy + 1
    india_coll12 = india
    world_coll12 = worlcolle
    budget12 = buged
    return coleee, india_coll12, budget12, world_coll12, verdi, day
def imdb(seach_input):
    seach_movie = "https://www.google.com/search?q="
    seach_movie1 ="&rlz=1C1RXQR_enIN930IN930&biw=1280&bih=601&sxsrf=AJOqlzVNqE_3ckZuDArKrajullgip_qHlQ%3A1678611194327&ei=-pINZMPKE8aL4-EPt6udiAY&ved=0ahUKEwjDr9D_gdb9AhXGxTgGHbdVB2EQ4dUDCA8&uact=5&oq="
    seach_movie2 = "&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIFCAAQgAQyBggAEBYQHjIFCAAQhgM6CggAEB4QogQQsAM6CAgAEKIEELADSgQIQRgBUJ4GWNAKYMAQaAFwAHgAgAGiAYgB-ASSAQMwLjSYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp"
    imbd_rating = requests.get(seach_movie+seach_input+" imdb&num=1"+seach_movie1+seach_input+" imdb"+seach_movie2)
    rating = BeautifulSoup(imbd_rating.content,"html.parser")
    rating = rating.find(class_ = "oqSTJd").text
    return rating

def other_movie(movie_nam):
    movie_nam = movie_nam.lower()
    movie_nam = movie_nam.replace(" ","-")
    day_by_day = requests.get('https://www.bollywoodhungama.com/movie/'+movie_nam+'/box-office/#bh-movie-box-office')
    movie_day_co = BeautifulSoup(day_by_day.content,"html.parser")
    movi11 = movie_day_co.find_all(class_ = 'tablesaw tablesaw-swipe')[2]
    movi12 = movi11.find_all('td')
    day = []
    coleee = []
    mm = 0
    nn = 2
    xx = 0
    for i in movi12:
        if xx == mm:
            day.append(i.text)
            mm = mm + 4
        if xx == nn:
            ii = i.text
            ii = ii[1:-4]
            coleee.append(float(ii))
            nn = nn + 4
        xx = xx + 1
    return coleee
