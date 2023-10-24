def f1And2(x):
    return 16*(x**3)-87*(x**2)+142*x-110

def f3(x):
    return 4*x**3+(185/8)*x**2-(217/4)*x+(249/4)

def bisectNTimes(minX, maxX, n, f):
    midX = (maxX + minX) / 2

    if n == 0 or f(midX) == 0:
        return midX

    if ((f(minX) * f(midX)) < 0):
        return bisectNTimes(minX, midX, n - 1, f)
    if ((f(maxX) * f(midX)) < 0):
        return bisectNTimes(midX, maxX, n - 1, f)
    print(minX, maxX, midX, n)

def convergeWithBisect(minX, maxX, f):
    x0 = (maxX + minX) / 2
    while(f(x0) != 0):
        x0 = (maxX + minX) / 2

        if ((f(minX) * f(x0)) < 0):
            maxX = x0
        if ((f(maxX) * f(x0)) < 0):
            minX = x0
    return x0

def getCheckedConvergedBisect(minX, maxX, f, bisect, n=None):
    x0 = bisect(minX, maxX, f) if n is None else bisect(minX, maxX, f, n)
    if (f(x0) != 0):
        print("Bisect is wrong, f(x0) does not equal 0")
    return x0

def getError(minX, maxX, n, f, bisect):
    return abs(bisect(minX, maxX, getCheckedConvergedBisect(minX, maxX, f, convergeWithBisect), f) - bisect(minX, maxX, n, f))


print(bisectNTimes(3, 4, 2, f1And2))

print(getError(1, 4, 3, f1And2, bisectNTimes))

print(getCheckedConvergedBisect(-8, -7, f3, convergeWithBisect))

