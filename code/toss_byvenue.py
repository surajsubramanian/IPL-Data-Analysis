import psycopg2
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

con = psycopg2.connect(database='ipl', user='suraj')
cur = con.cursor()

cur.execute("SELECT venue_name,count(match_id) from ipl_match where toss_decision = 'bat' group by venue_name order by count(match_id) desc")

a=[]
for item in cur:
    a.append(item)

sum=0

venue_toss_bat=dict(a)

cur.execute("SELECT venue_name,count(match_id) from ipl_match where toss_decision = 'field' group by venue_name order by count(match_id) desc")

a=[]
for item in cur:
    a.append(item)


venue_toss_field=dict(a)


X = np.arange(len(venue_toss_bat))
ax = plt.subplot(111)
ax.bar(X, venue_toss_bat.values(), width=0.2, color='b', align='center')
ax.bar(X-0.2, venue_toss_field.values(), width=0.2, color='g', align='center')
ax.legend(('Bat','Field'))
plt.xticks(X, venue_toss_bat.keys())
plt.title("TOSS CHOICE BY VENUE", fontsize=17)
plt.show()
