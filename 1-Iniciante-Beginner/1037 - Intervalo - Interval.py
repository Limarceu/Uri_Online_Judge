def intervalo(teste):
    if 0<=teste<=25: print('Intervalo [0,25]')
    elif 25<teste<=50: print('Intervalo (25,50]')
    elif 50<teste<=75: print('Intervalo (50,75]')
    elif 75<teste<=100: print('Intervalo (75,100]')
    else: print('Fora de intervalo')
    

if __name__ == '__main__':
    entrada = float(input())
    intervalo(entrada)
