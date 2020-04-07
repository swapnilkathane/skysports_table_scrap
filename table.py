import pandas
import requests
from bs4 import BeautifulSoup as bs
name=[]
points=[]
url='https://www.skysports.com/premier-league-table'
data = requests.get(url)
soup=bs(data.text , 'html.parser')
league_table = soup.find('table', class_="standing-table__table callfn")
#print(league_table)
for team in league_table.find_all('tbody'):
    rows=team.find_all('tr')
    for row in rows:
        team_name=row.find('td',class_="standing-table__cell standing-table__cell--name" ).text.strip()
        team_points=row.find_all('td', class_="standing-table__cell")[9].text.strip()
        name.append(team_name)
        points.append(team_points)
dict = {'Team name' : name, 'Points' : points}

df=pandas.DataFrame(dict)
df.to_csv('first.csv')