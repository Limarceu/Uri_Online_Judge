#Soma Simples - Simple Sum
def soma(a,b):
    '''
    To sum two entries.
        Parameters:
            a (int): An integer value
            b (int): An integer value
        Returns:
            sum (int): The sum of two integers
    '''
    return a+b

if __name__ == '__main__':
    A = int(input())
    B = int(input())
    SOMA = soma(A,B)
    print(f'SOMA = {SOMA}')
