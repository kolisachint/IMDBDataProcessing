# IMPORTING REQUIRED LIBRARY

import os
import sys
import requests
import BeautifulSoup
from requests import get


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])  













=======
>>>>>>> refs/heads/master
