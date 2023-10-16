from config import logger, headers
from rich import print
from pprint import pprint as prt
from selectolax.parser import HTMLParser
import httpx
from models import Planet

url = "https://www.drikpanchang.com/planet/position/planetary-positions-sidereal.html?date=01/01/1991&time=00:00:00"


def get_content(resp):
    return HTMLParser(resp.text)


def load_data(url) -> HTMLParser:
    client = httpx.Client(headers=headers)
    resp = client.get(url)
    return get_content(resp)


def get_data(url: str):
    html = load_data(url)
    data = []
    for item in html.css("div.dpPlanetCard"):
        name = item.css_first("div.dpCardTitle div").text(strip=True)
        content_data = {}
        for content in item.css("div.dpPlanetCardContent"):
            title = content.css_first("span.dpTitle").text(strip=True).lower().replace(' ', '_').replace('/', '_')
            value = content.css_first("span.dpValue").text(strip=True)
            content_data.update({f"{title}": value})
            # longitude = item.css_first('div.dpPlanetCardContent span.dpValue').text(strip=True)
            # latitude = item.css_first('div.dpPlanetCardContent span.dpValue').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # name = item.css_first('div.dpCardTitle div').text(strip=True)
        # prt(content_data)
        data.append(Planet(name=name, planet_data=content_data))
           
    return data


@logger.catch
def main():
    data = get_data(url)
    json_data = [model.json() for model in data]
    print(json_data)


if __name__ == "__main__":
    main()
