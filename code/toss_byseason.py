import psycopg2
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

con = psycopg2.connect(database='ipl', user='suraj')
cur = con.cursor()

cur.execute("SELECT count(match_id) from ipl_match where toss_decision = 'bat' group by season_id")

season_toss_bat = {}
i=1
for t in cur:
    for j in t:
        season_toss_bat[i]=j
    i+=1

cur.execute("SELECT count(match_id) from ipl_match where toss_decision = 'field' group by season_id")

season_toss_field = {}
i=1
for t in cur:
    for j in t:
        season_toss_field[i]=j
    i+=1

cur.execute("SELECT season_id from season")

seasons = []
for i in cur:
    for j in i:
        seasons.append(j)

print(seasons)
print(season_toss_bat)
print(season_toss_field)

#width=0.25
#
#plt.bar(range(len(season_toss_bat)), list(season_toss_bat.values()), align='center', color='g')
#plt.xticks(range(len(season_toss_bat)), list(season_toss_bat.keys()))
#
#plt.bar(range(len(season_toss_field)), list(season_toss_field.values()), align='center')
#plt.xticks(range(len(season_toss_field)), list(season_toss_field.keys()))

X = np.arange(len(season_toss_bat))
ax = plt.subplot(111)
ax.bar(X, season_toss_bat.values(), width=0.2, color='b', align='center')
ax.bar(X-0.2, season_toss_field.values(), width=0.2, color='g', align='center')
ax.legend(('bat','field') )
plt.xticks(X, season_toss_bat.keys())
plt.title("TOSS DECISIONS", fontsize=17)


plt.show()
