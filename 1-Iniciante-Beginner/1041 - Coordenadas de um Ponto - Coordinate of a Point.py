def xy(px , py):
    if px > 0 and py > 0: print('Q1')
    elif px < 0 and py > 0: print('Q2')
    elif px < 0 and py < 0: print('Q3')
    elif px > 0 and py < 0: print('Q4')
    elif px == 0 and py != 0: print('Eixo Y')
    elif px != 0 and py == 0: print('Eixo X')
    else: print('Origem')
    
if __name__ == '__main__':
    x, y = input().split()
    xy(float(x), float(y))
