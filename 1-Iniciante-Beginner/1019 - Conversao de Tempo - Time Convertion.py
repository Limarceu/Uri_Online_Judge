def seg_to_hh(seg):
    h = seg//3600
    m = seg%3600//60
    s = seg%3600%60
    return f'{h}:{m}:{s}'

if __name__ == '__main__':
    segundos = int(input())
    horas = seg_to_hh(segundos)
    print(horas)
