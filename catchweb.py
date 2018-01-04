import urllib
import bs4
import random

headers=[
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
        {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]


number=1

for i in range(0,250):
    url="https://book.douban.com/top250?start=0"+str(i)
    page_request=urllib.request.Request(url,headers=random.choice(headers))
    response=urllib.request.urlopen(page_request)

    soup=bs4.BeautifulSoup(response,"lxml")
    table=soup.find(attrs={"class":"pl2"})
    nameOfBook=table.find("a")
    nameOfBook=nameOfBook.text
    nameOfBook=nameOfBook.replace("\n","") ##字符串处理
    nameOfBook=nameOfBook.strip()
    print(nameOfBook)
    print(number)
    number+=1
