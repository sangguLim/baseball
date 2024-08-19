import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url_base = 'https://www.koreabaseball.com/Record/Player/{category}'
category_list = ['HitterBasic/Basic1.aspx', 'PitcherBasic/Basic1.aspx', 
                 'Defense/Basic.aspx', 'Runner/Basic.aspx']
                 
for category in category_list:
    url = url_base.format(category = category)