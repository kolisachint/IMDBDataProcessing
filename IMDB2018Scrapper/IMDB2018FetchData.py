import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

OUTPUT_PATH = os.environ.get('IMDB_OUTPUT_PATH', '/home/kolisachint/IMDB/movie_ratings.csv')
IMDB_URL = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'


def fetch_movie_data(url):
    """Fetch and parse movie data from IMDB search page."""
    headers = {'Accept-Language': 'en-US,en;q=0.5'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
    print(f"Found {len(movie_containers)} movie containers")

    names, years, imdb_ratings, metascores, votes = [], [], [], [], []

    for container in movie_containers:
        # Only process movies that have a MetaScore
        if container.find('div', class_='ratings-metascore') is None:
            continue

        names.append(container.h3.a.text)
        years.append(container.h3.find('span', class_='lister-item-year').text)
        imdb_ratings.append(float(container.strong.text))
        metascores.append(int(container.find('span', class_='metascore').text.strip()))
        votes.append(int(container.find('span', attrs={'name': 'nv'})['data-value']))

    return pd.DataFrame({
        'movie': names,
        'year': years,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
    })


def main():
    movie_ratings = fetch_movie_data(IMDB_URL)
    print(movie_ratings.head(10))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    movie_ratings.to_csv(OUTPUT_PATH, sep='|', index=False)
    print(f"Saved {len(movie_ratings)} records to {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
