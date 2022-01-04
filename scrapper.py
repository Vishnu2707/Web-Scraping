import requests                                            #to fetch the url
from bs4 import BeautifulSoup                              #this is to parse through the data that we fetched.

URL = "https://www.worldometers.info/coronavirus/country/india" 
#URL = "https://www.worldometers.info/coronavirus/"            world data  

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

soup1 = BeautifulSoup(soup.prettify(), "html.parser")               #formatting the data

date = soup1.find_all('div',style = "font-size:13px; color:#999; text-align:center")

print(date[0].text.strip(),"\n")

cases = soup1.find_all('div', class_= "maincounter-number")


print("Corona virus cases :- ",cases[0].text.strip(),"\n")
print("Deaths :- ",cases[1].text.strip(),"\n")
print("Recovered :- ",cases[2].text.strip(),"\n")