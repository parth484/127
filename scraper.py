from bs4 import BeautifulSoup as bs
import pandas as pd


BRIGHTSTARS_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

soup = BeautifulSoup(browser.page_source, "html.parser")

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df = pd.DataFrame(list,columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)

df.to_csv('bright_stars.csv')