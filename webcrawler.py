from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def Filters():
    isValid = False
    while(isValid == False):
        opc1 = "Type 1 if you want the entries with more than 5 words in the title.\n"
        opc2 = "Type 2 if you want the entries 5 words or less\n"
        opc3 = "Type 3 if you don't want to use filters\n"
        try:
            type = int(input(opc1 + opc2 + opc3))
            if(type == 1):
                isValid = True
                selectedFilter = 1
            elif(type == 2):
                isValid = True
                selectedFilter = 2
            elif(type == 3):
                isValid = True
                selectedFilter = 3
            else:
                print("Invalid! Please type a number between 1 and 2")
        except ValueError:
            print('Invalid! Please type a number')

    return selectedFilter


def searchRank(row):
    return row.find('span', {'class': 'rank'}).get_text()


def searchPoints(row):
    if(row.next_sibling.find('span', {'class': 'score'}) != None):
        point = row.next_sibling.find(
            'span', {'class': 'score'}).get_text()
    else:
        point = 'None'

    return point


def searchComments(row):
    if(row.next_sibling.find('a', text=re.compile('comments'), href=re.compile('item')) != None):
        comment = row.next_sibling.find('a', text=re.compile(
            'comments'), href=re.compile('item')).get_text()
    else:
        comment = 'None'

    return comment

def web(filter):
    url = 'https://news.ycombinator.com/'
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, 'html.parser')
    titles = []
    ranks = []
    comments = []
    points = []

    for row in s.find_all('tr', {'class': 'athing'}, limit=30):
        title = row.find('a', {'class': 'titlelink'}).get_text()

        if(filter == 1 and len(title.split()) > 5):
            rank = searchRank(row)
            point = searchPoints(row)
            comment = searchComments(row)

            titles.append(title)
            ranks.append(rank)
            points.append(point)
            comments.append(comment)
        elif(filter == 2 and len(title.split()) <= 5):
            rank = searchRank(row)
            point = searchPoints(row)
            comment = searchComments(row)

            titles.append(title)
            ranks.append(rank)
            points.append(point)
            comments.append(comment)
        elif(filter == 3):
            rank = searchRank(row)
            point = searchPoints(row)
            comment = searchComments(row)

            titles.append(title)
            ranks.append(rank)
            points.append(point)
            comments.append(comment)

    dataFrame = pd.DataFrame()
    dataFrame['Titles'] = titles
    dataFrame['Ranks'] = ranks
    dataFrame['Points'] = points
    dataFrame['Comments'] = comments

    print(dataFrame)


web(Filters())
