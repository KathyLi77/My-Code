#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:52:11 2022

@author: Jiaqi Li, Jiehao Xing
"""
print('The authors are Jiaqi Li and Jiehao Xing. Welcome to our program!')

#Importing the modules
import webbrowser as wb
import requests as rq
import bs4

#Read html file
test_html_file=open('test.html')
html_soup=bs4.BeautifulSoup(test_html_file.read(),features='lxml')

#finding anchor command
links_content=html_soup.find_all("a")

#printing the number of links
number_of_links=str(len(links_content))
print("There are "+number_of_links+" links in the file. ")

#extracting links from lines
pure_links=[]
for tag in links_content:
    purelink=tag.get('href', None)
    if purelink is not None:
        pure_links.append(purelink)
        
#printing out links
print("Here are the links extracted! ")

for i in range(len(pure_links)):
    print(pure_links[i])

#test links and print the error links    
for i in range(len(pure_links)):
    res=rq.get(pure_links[i])
    if res.status_code != 200:
        print('ERROR – '+ pure_links[i])

#opening link 1
print("Now opening the first link!")
page_to_open=wb.get('firefox') #question
page_to_open.open(pure_links[0]) 

