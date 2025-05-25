def mdc(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError('a e b precisam ser números naturais diferentes de 0')
    
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

try:
    print(mdc(48,18)) #6
    print(mdc(17,29)) #1
    print(mdc(0,5)) #Erro
except ValueError as e:
    print(e)