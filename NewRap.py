import math


print("""Look, if you had one shot or one opportunity
To seize everything you ever wanted in one moment
Would you capture it, or just let it slip? Yo""")

def f4(x):
    return (4)*x**3+(89/4)*x**2-(105/2)*x+(121/2)

def f5(x):
    return math.sin(x) - (6/10) * x
    
def df4(x):
    return (12)*x**2+(89/2)*x-(105/2)
    
def df5(x):
    return math.cos(x) - 6/10

def newRap(x, n, f, df):
    if (n == 0):
        return x
    return newRap(x - f(x) / df(x), n - 1, f, df)


print(newRap(-7, 3, f4, df4))
print(newRap(-7, 18, f4, df4))

print(newRap(1, 100, f5, df5))
print(f5(newRap(1, 100, f5, df5)))