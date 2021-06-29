a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

maior_ab = (a+b+abs(a-b))/2
maior_ab_c = int((maior_ab + c + abs(maior_ab - c))/2)

print('{} eh o maior'.format(maior_ab_c))