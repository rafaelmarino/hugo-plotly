import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys


def text2float(text):
    """Convert a string to a float where appropriate, else return 0"""
    try:
        return float(text)
    except ValueError:
        return 0


def scrape_f1_2021_wdc():
    """Scrape F1 data and write two dataframes: normal and cumulative points"""

    url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-abu-dhabi-grand-prix/standings/drivers"

    # request
    r = requests.get(url)
    print(f"Request status code: {r.status_code}")
    print(f"Request encoding: {r.encoding}")  # UTF-8
    print(f"Request size in kb {sys.getsizeof(r) / 1024}")  # 0.04kb
    #  r.text

    # make BeautifulSoup and scrape it
    soup = BeautifulSoup(r.text, "html.parser")
    tracks = soup.find_all(class_="_3QkVN")
    assert len(tracks) == 22  # 22 tracks
    all_points = []
    for track in tracks:
        points = [t.text for t in track.find_all(class_="_1BvfV")]
        points = [text2float(p) for p in points]
        assert len(points) == 21  # 21 drivers
        all_points.append(points)

    # create dataframes (raw and cumulative)
    colnames = "BHR ROM POR ESP MCO AZE FRA STY AUT GBR HUN BEL NLD ITA RUS TUR USA MEX BRA QAT SAU ARE".split()
    idx = "Verstappen Hamilton Bottas Pérez Sainz Norris Leclerc Ricciardo Gasly Alonso Ocon Vettel Stroll Tsunoda Russell Räikkönen Latifi Giovinazzi Schumacher Kubica Mazepin".split()

    df1 = pd.DataFrame(all_points).transpose()
    df1.columns = colnames
    df1.index = idx
    df2 = df1.cumsum(axis=1)
    return df1, df2


if __name__ == "__main__":
    df1, df2 = scrape_f1_2021_wdc()
    df1.to_csv("data/wdc_points1.csv")
    df2.to_csv("data/wdc_points2.csv")
