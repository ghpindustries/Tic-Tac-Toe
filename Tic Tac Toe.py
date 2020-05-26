x,y,z= input().split(),input().split(),input().split()
xwin,owin = 0,0
#Horizontal Wins Check
for i in x:
    if x.count(i)==3 and i == 'X':
       print('Player X')
       xwin=1
       break
    elif x.count(i)==3 and i == 'O':
       print('Player O')
       owin = 1
       break
for i in y:
    if y.count(i)==3 and i == 'X':
       print('Player X')
       xwin=1
       break
    elif y.count(i)==3 and i == 'O':
       print('Player O')
       owin = 1
       break
for i in z:
    if z.count(i)==3 and i == 'X':
       print('Player X')
       xwin=1
       break
    elif z.count(i)==3 and i == 'O':
       print('Player O')
       owin = 1
       break
#Vertical Wins Check
vx = list(x[0]+y[0]+z[0])
vy = list(x[1]+y[1]+z[1])
vz = list(x[2]+y[2]+z[2])

if xwin ==0 and owin ==0:
   for i in vx:
      if vx.count(i)==3 and i == 'X':
         print('Player X')
         xwin=1
         break
      elif vx.count(i)==3 and i == 'O':
         print('Player O')
         owin = 1
         break
   for i in vy:
      if vy.count(i)==3 and i == 'X':
         print('Player X')
         xwin=1
         break
      elif vy.count(i)==3 and i == 'O':
         print('Player O')
         owin = 1
         break
   for i in vz:
      if vz.count(i)==3 and i == 'X':
         print('Player X')
         xwin=1
         break
      elif vz.count(i)==3 and i == 'O':
         print('Player O')
         owin = 1
         break
#Diagonal Wins Check

dx = list(x[0]+ y[1]+z[2])
dy = list(x[2]+ y[1] + z[0])
if xwin ==0 and owin ==0:
   for i in dx:
       if dx.count(i) == 3 and i=='X':
         print('Player X')
         xwin = 1
         break
       elif dx.count(i)==3 and i == 'O':
         print('Player O')
         owin = 1
         break
   for i in dy:
      if dy.count(i)==3 and i == 'X':
         print('Player X')
         xwin=1
         break
      elif dy.count(i)==3 and i == 'O':
         print('Player O')
         owin = 1
         break
if xwin ==0 and owin==0:
   print('Tie')
