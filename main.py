import requests 
import json
from bs4 import BeautifulSoup 
headers=["crop","quantity","price"]
URL = "https://rates.goldenchennai.com/vegetable-price/tamil-nadu-vegetable-price-today/#cities"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
table=soup.find('tbody')
data=[]
for row in table.find_all('tr'):
    t_row={}
    for table_data,table_headers in zip(row.find_all('td'),headers):
       t_row[table_headers]=table_data.text.replace('n',"").strip()
    
    data.append(t_row)
json_data=json.dumps(data)
print(json_data)