def mdc(a: int, b:int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError('a e b precisam ser naturais diferentes de 0')
    
    c = a % b

    if c == 0:
        return b
    else:
        return mdc(b, c)

try:
    print(mdc(48, 18)) # 6
    print(mdc(0, 5)) # Erro
except ValueError as e:
    print(e)