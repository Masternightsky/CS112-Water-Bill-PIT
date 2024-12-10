from decimal import *
getcontext().prec = 5

Previous = 356
Present = 388
Half = Decimal('218.40')
TQ = Decimal('349.40')     #Three Quarters
Whole = Decimal('698.85')
WHalf = Decimal('1747.20')
Two = Decimal('4368.00')
Three = Decimal('7862.40')
Four = Decimal('15724.80')
Ten = Decimal('60278.40')
CuM = Present - Previous

def bracketing():
    global CuM
    global Half
    Amount = Half
    while CuM > 10:
        if CuM > 41:
            while CuM >= 41:
                CuM -= 1
                Amount = Decimal(Amount) + Decimal('36.00')
        elif CuM > 31:
            while CuM >= 31:
                CuM -= 1
                Amount = Decimal(Amount) + Decimal('33.65')
        elif CuM > 21:
            while CuM >= 21:
                CuM -= 1
                Amount = Decimal(Amount) + Decimal('31.85')
        elif CuM > 11:
            while CuM >= 11:
                CuM -= 1
                Amount = Decimal(Amount) + Decimal('30.55')
            print(CuM)
            print(Amount)            
bracketing()