import requests
from bs4 import BeautifulSoup
import pandas as pd

items = []
for i in range(1, 101):
    url = f"https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-{i}"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    item_cell = soup.find('div', class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    for item in item_cell:
        try:
            id = item.find('div', class_="item-container").get('id')
        except AttributeError:
            id = None

        try:
            title = item.find('a', class_="item-title").text
        except AttributeError:
            title = None

        try:
            brand = item.find('div', class_="item-branding has-brand-store").img['title']
        except (AttributeError,TypeError):
            brand = None

        try:
            rating = item.find('a', class_="item-rating")['title'][-3:]
        except (AttributeError, TypeError):
            rating = None

        try:
            rating_count = item.find('span', class_="item-rating-num").text[1:-1]
        except AttributeError:
            rating_count = None

        try:
            pricing_text = item.find('li', class_="price-current").text.split()[0][1:]
        except (AttributeError, IndexError):
            pricing_text = None

        try:
            shipping = item.find("li", class_="price-ship").text
        except AttributeError:
            shipping = None

        try:
            image_url = item.find('a', class_="item-img").img['src']
        except (AttributeError, TypeError):
            image_url = None

        try:
            item_features = item.find('ul', class_='item-features')
            if item_features:
                li_tags = item_features.find_all('li')
                features = []
                for li_tag in li_tags:
                    strong_tag = li_tag.find('strong')
                    if strong_tag:
                        label = strong_tag.text
                        value = li_tag.text.replace(label, '').strip()
                        features.append((label, value))
                item_features = features
            else:
                item_features = None
        except AttributeError:
            item_features = None

        items.append((id, title, brand, rating, rating_count, pricing_text, shipping, image_url, str(item_features)))

df = pd.DataFrame(items, columns=['id', 'title', 'brand', 'rating', 'rating_count', 'pricing', 'shipping', 'Image_URL', 'item_features'])
df.to_csv('item.csv')
