import numpy as np

pattern = [
    [0, 0], 
    [0, 1], 
    [1, 0], 
    [1, 1],
    ]

def AND(a:int, b:int)->int:
    x = np.array([a, b])
    weight = np.array([0.5, 0.5])
    bias = -0.7

    temp = np.sum(x*weight) + bias

    if temp > 0:
        return 1
    elif temp <= 0:
        return 0
    
def NAND(a:int, b:int)->int:
    x = np.array([a, b])
    weight = np.array([-0.5, -0.5])
    bias = 0.7

    temp = np.sum(x*weight) + bias

    if temp > 0:
        return 1
    elif temp <= 0:
        return 0

def OR(a:int, b:int)->int:
    x = np.array([a, b])
    weight = np.array([0.5, 0.5])
    bias = -0.2

    temp = np.sum(x*weight) + bias

    if temp > 0:
        return 1
    elif temp <= 0:
        return 0
    
def XOR(a:int, b:int)->int:
    s1 = NAND(a, b)
    s2 = OR(a, b)
    return AND(s1, s2)

def doAND()->None:
    for a, b in pattern:
        print(f"[{a}, {b}] >>> {AND(a, b)}")

def doNAND()->None:
    for a, b in pattern:
        print(f"[{a}, {b}] >>> {NAND(a, b)}")

def doOR()->None:
    for a, b in pattern:
        print(f"[{a}, {b}] >>> {OR(a, b)}")

def doXOR()->None:
    for a, b in pattern:
        print(f"[{a}, {b}] >>> {XOR(a, b)}")
    
if __name__=="__main__":
    doAND()
    print("")
    doNAND()
    print("")
    doOR()
    print("")
    doXOR()