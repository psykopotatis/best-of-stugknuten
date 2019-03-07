import requests
from bs4 import BeautifulSoup
import pickler


base_url = 'https://www.stugknuten.com'

def get_url(page):
    url = 'https://www.stugknuten.com/resultatnysokning.asp?ort=%C3%B6land&page='
    return url + str(page)

def get_soup(url):
    print('[GET] ' + url)
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse_soup(soup):
    result = []
    elements = soup.find_all('article', class_='CottageCard')

    for element in elements:
        image_url = get_image_url(element)

        listing_title = element.find('a', class_='Listing-title')
        title = listing_title.string.strip()
        href = listing_title.get('href')
        print(title)
        print(href)

        location = element.find('h3', class_='CottageLocation').string.strip()
        print(location)
        cottage = {
            'title': title,
            'location': location,
            'href': href,
            'image_url': image_url
        }

        result.append(cottage)

    return result

def get_image_url(element):
    image_div = element.find('div', class_='CottageCard-image-img')
    print(image_div)
    style = image_div.get('style')
    print(style)
    image_url = style.replace('background-image: url(', '')[:-2]
    print(image_url)
    return base_url + image_url


def get_links():
    links = []
    for page_number in range(1, 16):
        page_url = get_url(page_number)
        page_soup = get_soup(page_url)
        page_links = parse_soup(page_soup)
        links.extend(page_links)
    return links

###############################################################################

urls = get_links()
pickler.save('stugor_oland.pickle', urls)
