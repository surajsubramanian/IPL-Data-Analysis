import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import psycopg2
import sys

con = psycopg2.connect(database='ipl', user='suraj')
cur = con.cursor()
cur.execute('''SELECT team_short_code,count (ipl_match)
            from ipl_match, team_ipl
            where ipl_match.match_winner_id = team_ipl.team_id
            GROUP BY team_short_code
            ORDER BY count (ipl_match) desc''')

a=[]

for item in cur:
    a.append(item)
a = dict (a)
print(a)


k=[]
v=[]

for key,value in a.items():
    k.append(key)
    v.append(value)
plt.bar(k,v)
plt.show()
