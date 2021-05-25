import random
display = drivers.Lcd()

with open('dinners.txt') as f:
    lines = f.readlines()

x=0
for dinner in lines:
    lines[x] = dinner.strip()
    x+=1

rand = random.randrange(len(lines))
choice = lines[rand]

display.lcd_display_string(choice, 1)
