from math import floor
h0,m0,h1,m1 = input().split()

n1 = (int(h0)+int(m0)/60)
n2 = (int(h1)+int(m1)/60)
t=n2-n1
if t>=1:
    pt = floor(t)
    tt = round((t%pt)*60)
elif 0<t<1:
    pt = 0
    tt=round(t*60)
elif t<0:
    pt = floor(24 + t)
    tt = round(((24 + t)%pt)*60)
else:
    pt = 24
    tt = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(pt,tt))
