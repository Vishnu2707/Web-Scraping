import requests                                            #to fetch the url
from bs4 import BeautifulSoup                              #this is to parse through the data that we fetched.

URL = "https://www.amazon.com/India-Tree-Rainbow-Pepper-Pantry/dp/B07XK81DYY/ref=sr_1_5?adgrpid=1338106518018791&hvadid=83631787970864&hvbmt=be&hvdev=c&hvlocphy=1661&hvnetw=o&hvqmt=e&hvtargid=kwd-83632285155786&hydadcr=24663_13493294&keywords=amazon+india&qid=1641310192&sr=8-5"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

soup1 = BeautifulSoup(soup.prettify(), "html.parser")               #formatting the data

title = soup1.find(id="productTitle").get_text()

print(title.strip())