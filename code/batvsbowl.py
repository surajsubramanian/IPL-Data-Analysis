import matplotlib
matplotlib.use('TkAgg')

import psycopg2
import csv
import sys
import pprint
from collections import OrderedDict
con = psycopg2.connect(database='ipl', user='suraj')
cur = con.cursor()

batsman = input ("Enter batsman name: ")
bowler = input ("Enter bowler name: ")

cur.execute('''SELECT player_id
                            from player_ipl
                            where player_name = (%s)''',(bowler,))

bowler_id = cur.fetchone()

batsman_id = cur.execute('''SELECT player_id
    from player_ipl
    where player_name = (%s)''',(batsman,))

batsman_id = cur.fetchone()


for i in bowler_id:
    bowler_id = i

for i in batsman_id:
    batsman_id = i

print(batsman_id)
print(bowler_id)

balls=0
runs=0
wickets=0
strike_rate=0
dots=0
four=0
six=0

f = open("/Users/suraj/Desktop/CRICTICS/ballbyball/Ball_by_Ball.csv")
records = csv.DictReader(f)
for row in records:
    row = dict(row)
    
    
    if(int(row['Striker_Id']) == batsman_id and int(row['Bowler_Id']) == bowler_id):
        runs += int(row['Batsman_Scored'])
        balls += 1
        if(row['Player_dissimal_Id'] != ' ' ):
            wickets += 1
        if(int(row['Batsman_Scored'])==0):
            dots+=1
        if(int(row['Batsman_Scored'])==4):
            four+=1
        if(int(row['Batsman_Scored'])==6):
            six+=1

strike_rate = (runs/balls)*100
dots=dots-wickets

print("RUNS :", runs)
print("BALLS :", balls)
print("WICKETS :",wickets)
print("DOTS :",dots)
print("FOUR :",four)
print("SIX :",six)
print("STRIKE RATE:", strike_rate)
