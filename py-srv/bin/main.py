#!/usr/bin/env python
import graphene
import extraction
import requests

def extract(url):
    html = requests.get(url).text
    extracted = extraction.Extractor().extract(html, source_url=url)
    return extracted

def main():
    val = extract("http://nodejs-srv:8000/")
    print(val)

if __name__ == '__main__':
    main()
