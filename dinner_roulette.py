import random

with open('dinners.txt') as f:
    lines = f.readlines()

x=0
for dinner in lines:
    lines[x] = dinner.strip()
    x+=1

rand = random.randrange(len(lines))
choice = lines[rand]
print(choice)
