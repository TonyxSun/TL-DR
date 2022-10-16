
import requests
from bs4 import BeautifulSoup
import validators
import re
from urllib.request import urlopen

def validateUrl(url):
    valid=validators.url(url)
    if valid==True or url.rfind(".com") != -1 or url.rfind(".ca") != -1:
        print("Url is valid")
        return True
    else:
        print("Invalid url")
        return False

def scrape(url):
    try:
        if "wikipedia" in url:
            source = urlopen(url).read()
            soup = BeautifulSoup(source,'lxml')
            text = ''
            for paragraph in soup.find_all('p'):
                text += paragraph.text
            text = re.sub(r'\[.*?\]+', '', text)
            text = text.replace('\n', '')
            return text
        else:
            # getting response object
            res = requests.get(url)
            
            # Initialize the object with the document
            soup = BeautifulSoup(res.content, "html.parser")
            
            out = ""
            for para in soup.find_all("p"):
                text = para.get_text()
                # reduce misc outputs
                if len(text.split(" ")) > 3:
                    out += text
            return out
    except:
        return "Failed to open url."

# if __name__  == "__main__":
#     # validateUrl("gist.github.com/dperini/729294")
#     # # url of the website
#     # doc = "https://javascdeep--8965d4e409d3"
#     # print(scrape(doc))
#     # response = requests.get(
# 	# url="https://en.wikipedia.org/wiki/Web_scraping",
# # )
#     url = "https://en.wikipedia.org/wiki/Web_scraping"
#     if validateUrl(url):
#         scrape(url)

# supported:
# https://www.msn.com/en-ca/news/other/joe-biden-s-comment-on-california-gas-prices-left-both-allies-and-adversaries-confused/ar-AA1306dD?ocid=msedgntp&cvid=fd6cece1daba482ee491c00e7821927d

