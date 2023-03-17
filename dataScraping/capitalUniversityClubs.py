from bs4 import BeautifulSoup4
import requests

base_url = "https://www.capital.edu/"
urls = ["Academic-and-Professional", "Community-Leadership", "Cultural-Diversity/", "Fraternity-and-Sorority-Life", "Arts-and-Media", "Religious-and-Spiritual", "Service", "Social-and-Recreational", "Special-Interest-Groups"]
# religious and spiritual is not available

url = base_url + urls[0]
req = requests.get(url)