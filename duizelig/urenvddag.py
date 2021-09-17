x = 0

while x <=23:
    if x >= 0 and x <= 11:
        print(x,"AM")
    if x >= 12 and x <= 23:
        print(x,"PM")
    if x == 24:
        break
    x = x + 1