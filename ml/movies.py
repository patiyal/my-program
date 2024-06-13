import streamlit as st
import pandas as pd
import top_10, day_by_day, comment_anali, top_100
import plotly.express as px
movie_sidebar = st.sidebar.radio(
    'Select any Option',
    ('Movie Collection','Top Year by Year','Top 100 Movie','Movie Comment','top 10 year')
)
if movie_sidebar == 'Movie Collection':
    movie_name = st.sidebar.text_input('Search Movie Name')
    st.sidebar.button('Search')
        # st.write('movie ka name ye hai',movie_name)
    st.title('Movie Overview')
    alll_day_cole, india_colle12, budget12, world_coll12, verdi, day = day_by_day.all_day(movie_name)
    col1 , col2, col3 = st.columns(3)
    with col1:
        st.header('Movie Name')
        st.title(movie_name)
    with col2:
        st.header('IMDB Rating')
        rating = day_by_day.imdb(movie_name)
        st.title(rating)
    with col3:
        st.header('World')
        st.title(world_coll12+"cr")
    col1 , col2, col3 = st.columns(3)
    with col1:
        st.header('India')
        st.title(india_colle12+'cr')
    with col2:
        st.header('Budget')
        st.title(budget12+"cr")
    with col3:
        st.header('Verdict')
        st.title(verdi)
    # with col3:
    #     st.header('Wolrd Collection')
    #     st.title("500cr")
    # st.write("IMDB Rating = 6.9")
    # st.write("world wide box = 31")
    # st.write('india collection = 24')
    charrt = st.selectbox('Select Charts',['bar', 'scater', 'pie', 'line'])
    if charrt == 'bar':
        fig = px.bar(y=alll_day_cole, x= day, text_auto='.2')
        st.plotly_chart(fig)
    if charrt == 'scater':
        fig = px.scatter(y=alll_day_cole, x= day)
        st.plotly_chart(fig)
    if charrt == 'pie':
        fig = px.pie(values=alll_day_cole, names= day)
        st.plotly_chart(fig)
    if charrt == 'line':
        fig = px.line(y=alll_day_cole)
        st.plotly_chart(fig)
    # fig1 = px.bar(y=alll_day_cole)
    # st.plotly_chart(fig1)
    st.title('Compare with other')
    new_movie  = st.text_input('Enter compare movie name fgh')
    if st.button('Sreachyu'):
        # st.write(new_movie, movie_name)
        new_name = day_by_day.other_movie(new_movie)
        fig = px.line(y=alll_day_cole)
        fig.add_scatter(y=new_name)
        st.plotly_chart(fig)

if movie_sidebar == 'top 10 year':
    year = [1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    year1 = st.sidebar.selectbox("Year", year)
    if st.sidebar.button('show'):
        # st.write(year1)
        top_10_movie_year, name_movi = top_10.top_11(year1)
        # st.write(top_10_movie_year)
        fig = px.bar(y=top_10_movie_year, x=name_movi)
        st.plotly_chart(fig)

if movie_sidebar == 'Movie Comment':
    movie_name = st.sidebar.text_input('Search Movie Name')
    if st.sidebar.button('Search'):
        # st.write('movie ka name ye hai',movie_name)
        commet, sentimen = comment_anali.coment_analis(movie_name)
        # st.write(commet[0])
        for i in range(0,25):
            if sentimen[i] == 1:
                st.success(commet[0][i])
            else:
                st.error(commet[0][i])
    
if movie_sidebar == 'Top 100 Movie':
    mo_co = top_100.top_100_movie("g")
    st.title("Top Movies by World Collection")
    fig = px.bar(mo_co, y='World Collection',hover_data=['Movie Name'],color='Verdict')
    st.plotly_chart(fig)
    st.title("Top Movies by India Collection")
    fig = px.bar(mo_co, y='India Collection',hover_data=['Movie Name'],color='Verdict')
    st.plotly_chart(fig)
    chart = st.selectbox("Charts",['Scater', 'bar', 'pie', 'histo gram', 'line'])
    if chart == 'Scater':
        fig = px.scatter(mo_co, x='World Collection',y='India Collection',hover_data=['Movie Name'],color='Verdict')
        st.plotly_chart(fig)
    if chart == 'bar':
        fig = px.bar(mo_co, y='World Collection',hover_data=['Movie Name'],color='India Collection')
        st.plotly_chart(fig)
    if chart == 'pie':
        fig = px.bar(mo_co, y='World Collection',hover_data=['Movie Name'],color='India Collection')
        st.plotly_chart(fig)
    if chart == 'histo gram':
        fig = px.histogram(mo_co['World Collection'])
        st.plotly_chart(fig)
    if chart == 'line':
        fig = px.line(mo_co,x= 'World Collection', y='Budget',hover_name='Movie Name')
        st.plotly_chart(fig)
    
