import psycopg2

con = psycopg2.connect(database='ipl', user='suraj')
cur = con.cursor()

cur.execute("SELECT count(match_id) from ipl_match where toss_decision = 'bat'")

for i in cur:
    t=i
for i in t:
    bat_toss=i

cur.execute("SELECT count(match_id) from ipl_match where toss_decision = 'field'")

for i in cur:
    t=i
for i in t:
    field_toss=i


cur.execute("SELECT count(match_id) from ipl_match")

for i in cur:
    t=i
for i in t:
    total_matches=i

print(bat_toss)
print(field_toss)
print(total_matches)

print("Toss decisions in %")
print("field", (field_toss/(bat_toss+field_toss))*100)
print("bat", (bat_toss/(bat_toss+field_toss))*100)
