Ll = 46.4
Ls = 15
tde = 0.576014
pl = 0.9
Ex = 1/pl
tde2 = tde * (1 - pl)

def Income(L):
    f1 = 14
    f2 = 2.5
    f3 = 3.6
    a = 3
    b = 15
    if L <= a:
        return f1
    elif L <= b:
        return f1 + (L - a) * f2
    else:
        return f1 + f2 * (b - a) + f3 * (L - b)


def OilCost(L):
    o = 0.088
    k = 7.13
    return L * o * k


def TimeOnTrip(L):
    alpha = 1
    beta = 1
    v = 64.7
    return L/(alpha * beta * v)

def AverageOnShort1(Ll,Ls):
    return (Income(Ls) * Ex + Income(Ll) - 2 * OilCost(Ls) * Ex - OilCost(Ll)) / (tde * Ex + 2 * Ex * TimeOnTrip(Ls) + TimeOnTrip(Ll))

def AverageOnLong(L):
    return(Income(L) - OilCost(L))/(tde + TimeOnTrip(L))

def AverageBefore(Ll,Ls):
    return (AverageOnLong(Ll) * pl + AverageOnShort1(Ll,Ls) * (1 - pl))


def SquareDiffBefore(Ll,Ls):
    return (pl * (AverageOnLong(Ll) - AverageBefore(Ll,Ls)) ** 2 + (1 - pl) * ((AverageOnShort1(Ll,Ls) - AverageBefore(Ll,Ls))) ** 2)

def AverageOnShort2(Ll,Ls):
    return (Income(Ls) * Ex + Income(Ll) - 2 * OilCost(Ls) * Ex - OilCost(Ll))/(tde + tde2 * (Ex - 1) + 2 * Ex * TimeOnTrip(Ls) + TimeOnTrip(Ll))

def AverageAfter(Ll,Ls):
    return (pl * AverageOnLong(Ll) + (1 - pl) * AverageOnShort2(Ll,Ls))

def SquareDiffAfter(Ll, Ls):
    return (pl * (AverageOnLong(Ll) - AverageAfter(Ll,Ls)) ** 2 + (1 - pl) * ((AverageOnShort2(Ll,Ls) - AverageAfter(Ll,Ls))) ** 2)

print("Average profit for short-distance taxi before adopting our plan",AverageOnShort1(Ll,Ls))
print("Average profit for short-distance taxi after adopting our plan",AverageOnShort2(Ll,Ls))

print("Average profit for long-distance taxi",AverageOnLong(Ll))

print("Average profit for all taxis before adopting our plan",AverageBefore(Ll,Ls))
print("Average profit for all taxis after adopting our plan",AverageAfter(Ll,Ls))

print("Square difference before adopting our plan: ",SquareDiffBefore(Ll,Ls))
print("Square difference after adopting our plan: ",SquareDiffAfter(Ll,Ls))

