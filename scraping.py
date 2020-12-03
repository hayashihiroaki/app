import requests
from bs4 import BeautifulSoup
import datetime

from assets.database import db_session
from assets.models import Data

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
    _results=get_udemy()

    sub = _results['subscribers']
    rev = _results['reviews']
    date=datetime.date.today()

    row = Data(date=date, subscribers=subscribers, reviews=reviews)

    db_session.add(row)
    db_session.commit()

if __name__=="__main__":
  write_date()