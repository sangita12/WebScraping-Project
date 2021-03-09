# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:02:50 2021

@author: cpl
"""


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plot
import pandas as pd

titles = []
reviews = []
ratings = []
ranks = []
page = 1

while page <= 41:   
    res = requests.get("https://www.trip.com/travel-guide/nepal-100079/tourist-attractions/"+ str(page) +".html")
    htmlPage = BeautifulSoup(res.text, 'html.parser')     
    placesCollection = htmlPage.find("div", {"class":"gl-poi-list_list"}).findAll("div", {"class":"burited_point"})
    
    for place in placesCollection:
        rank = ''
        title = ''
        review = ''
        rating = ''
        
        if place.find("h3", {"class":"list-content_title"}) is not None:
            title = place.find("h3", {"class":"list-content_title"}).get_text(strip = True)
        else:
            title = ''
            
        if place.find("span",{"class":"list-content_reviews"}) is not None:
            review = place.find("span",{"class":"list-content_reviews"}).get_text(strip = True)
        else:
            review = '0'
            
        if place.find("span", {'class':"gl-poi-list_rank_desc"}) is not None:
            rank = place.find("span", {'class':"gl-poi-list_rank_desc"}).get_text(strip = True)
        else:
            rank = ''
            
        if place.find("span",{'class':"fs3 list-content_rating"}) is not None:
            rating = place.find("span",{'class':"fs3 list-content_rating"}).get_text(strip = True)
        else:
            rating = 0
        
        titles.append(title)
        reviews.append(review.replace(' Reviews',''))
        ranks.append(rank)
        ratings.append(float(rating))
       
        page = page + 1
  

dataframe = pd.DataFrame(
    { 'Places': titles,
      'Reviews': reviews,
      'Rank': ranks,
      'Rating': ratings
      }
    )

dataframe.to_csv('Trip.csv')



