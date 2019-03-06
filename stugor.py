import requests
from bs4 import BeautifulSoup
import pickler
import json
import time



base_url = 'https://www.stugknuten.com'

def get_url(page):
    url = 'https://www.stugknuten.com/resultatnysokning.asp?page='
    return url + str(page)

def get_soup(url):
    print('[GET] ' + url)
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse_soup(soup):
    result = []
    """
    <a href="/stuga.asp?stugid=22317" class="Listing-title">
    					Hus uthyres i Stenungsunds kommun
    				</a>
    """
    anchor_tags = soup.find_all('a', class_='Listing-title')
    for anchor_tag in anchor_tags:
        href = anchor_tag.get('href')
        print(href)
        result.append(href)
    return(result)

def get_links():
    links = []
    for page_number in range(1, 435):
        page_url = get_url(page_number)
        page_soup = get_soup(page_url)
        page_links = parse_soup(page_soup)
        links.extend(page_links)
    return links

###############################################################################

urls = get_links()
pickler.save('urls.pickle', urls)
