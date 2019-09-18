#!/usr/bin/env python3
import urllib.request
CSV_FILE = "https://raw.githubusercontent.com/supportvectors/100datasets/master/warm-up/galton/galton-families.csv"
DATA_FILES = {
    "galton-families.csv": CSV_FILE
}

for k in  DATA_FILES:
    url = DATA_FILES[k]
    print("Downloading...{} <- {}".format(k, url))
    urllib.request.urlretrieve(url, k)


