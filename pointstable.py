
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

from sqlalchemy import create_engine

page = requests.get("https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/points-table")

soup = BeautifulSoup(page.text, features="lxml")

tb1 = soup.find("table", class_="table cb-srs-pnts")

col_names = [x.get_text() for x in tb1.find_all('td', class_="cb-srs-pnts-th")]

col_names[5] = 'pts'

team_names = [x.get_text() for x in tb1.find_all('td', class_="cb-srs-pnts-name")]

pnt_tb1 = [x.get_text() for x in tb1.find_all('td', class_="cb-srs-pnts-td")]

np_pnt_tb1 = (np.array(pnt_tb1)).reshape(len(team_names), 7)
np_pnt_tb1 = np.delete(np_pnt_tb1, 6, 1)
np_pnt_tb1 = np_pnt_tb1.astype(int)

consol_tb1 = pd.DataFrame(np_pnt_tb1, index=team_names, columns=col_names)
consol_tb1.columns.name = "Teams"

print(consol_tb1)

engine = create_engine('postgresql://suraj@localhost:5432/ipl')
consol_tb1.to_sql('Points_table', engine)


team_abr = []

for team in team_names:
    short_form=''
    for initial in team.split(' '):
        short_form = short_form + initial[0]
    team_abr.append(short_form)

title = ' IPL 2019 - MATCHES WON'
val_ticks = [1,2,3,4,5,6,7,8]
lost_ticks = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]

plt.bar(val_ticks, np_pnt_tb1[:,1],width=0.4,color='g',alpha=0.6,label='WON')

plt.bar(lost_ticks, np_pnt_tb1[:,2],width=0.4,color='r',alpha=0.6,label='LOST')

plt.yticks(val_ticks)
plt.ylabel("Matches")

plt.xticks(val_ticks, team_names, rotation='vertical')
plt.grid(True)

plt.legend()

plt.title(title)

plt.show()
