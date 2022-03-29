import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys

url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-abu-dhabi-grand-prix/standings/drivers"

# requests
r = requests.get(url)
print(r.status_code)
print(r.encoding)  # UTF-8
print(sys.getsizeof(r) / 1024)  # 0.04kb
#  r.text


def text2float(text):
    """Convert a string to a float where appropriate, else return 0"""
    try:
        return float(text)
    except ValueError:
        return 0


# scrape BeautifulSoup and create dataframe
soup = BeautifulSoup(r.text, "html.parser")
tracks = soup.find_all(class_="_3QkVN")
assert len(tracks) == 22  # 22 tracks
all_points = []
for track in tracks:
    points = [t.text for t in track.find_all(class_="_1BvfV")]
    points = [text2float(p) for p in points]
    assert len(points) == 21  # 21 drivers
    all_points.append(points)

colnames = "BHR ROM POR ESP MCO AZE FRA STY AUT GBR HUN BEL NLD ITA RUS TUR USA MEX BRA QAT SAU ARE".split()
idx = "Verstappen Hamilton Bottas Pérez Sainz Norris Leclerc Ricciardo Gasly Alonso Ocon Vettel Stroll Tsunoda Russell Räikkönen Latifi Giovinazzi Schumacher Kubica Mazepin".split()
df = pd.DataFrame(all_points).transpose()
df.columns = colnames
df.index = idx
df = df.cumsum(axis=1)
# df.to_csv("data/wdc_points2.csv")
