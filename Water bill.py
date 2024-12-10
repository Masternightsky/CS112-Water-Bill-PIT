from decimal import Decimal


Previous = 356
Present = 388
Half = 218.40
TQ = 349.40     #Three Quarters
Whole = 698.85
WHalf = 1747.20
Two = 4368.00
Three = 7862.40
Four = 15724.80
Ten = 60278.40
CuM = Present - Previous
Amount = Half

def bracketing():
    global CuM
    global Amount
    while CuM > 10:
        if CuM > 41:
            while CuM > 41:
                CuM -= 1
                Amount += 36.00
        elif CuM > 31:
            while CuM > 31:
                CuM -= 1
                Amount += 33.65
        elif CuM > 21:
            while CuM > 21:
                CuM -= 1
                Amount += 31.85
        elif CuM > 11:
            while CuM >= 11:
                CuM -= 1
                Amount += 30.55
            print(CuM)
            print(Decimal(str(Amount)))            
bracketing()