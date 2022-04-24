a = int(input("enter number of month as a figure:   "))
season = ['winter','spring','summer','autumn']
b = season
print(season)
if a >= 3:
   if a <= 5:
       print(b.pop(1))
if a >= 6:
    if a <= 8:
        print(b.pop(2))
if a >= 9:
    if a <= 11:
        print(b.pop(3))
if a >=1:
    if a <=2:
        print(b.pop(0))
if a == 12:
    print(b.pop(0))