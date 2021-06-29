a,b,c = input().split()
a,b,c = float(a),float(b),float(c)
atri = a*c/2
acir = 3.14159 * c**2
atra = c*(a+b)/2
aqua = b**2
aret = a*b

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(atri, acir, atra, aqua, aret))