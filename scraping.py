import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def get_udemy():
    url='https://scraping-for-beginner.herokuapp.com/udemy'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name=soup.select('.card-title')[0].string
    subscribers=soup.select('.subscribers')[0].string
    reviews=soup.select('.reviews')[0].string

    subscribers=int(subscribers.split('：')[1])
    reviews=int(reviews.split('：')[1])

    results={
        'name':name,
        'subscribers':subscribers,
        'reviews':reviews
    }

    return results

def write_date():
    df=pd.read_csv('assets/data.csv')

    _results=get_udemy()

    sub = _results['subscribers']
    rev = _results['reviews']
    date=datetime.datetime.today().strftime('%Y/%-m/%-d')

    results=pd.DataFrame([[date,sub,rev]],columns=['date','subscribers','reviews'])

    df=pd.concat([df,results])

    df.to_csv('assets/data.csv',index=False)

if __name__=="__main__":
  write_date()