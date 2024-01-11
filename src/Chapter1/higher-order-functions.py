def summation(n,fn):
    """
    高阶函数
    """
    total,k = 0,1
    while k<=n:
        total,k = total+fn(k),k+1
    return total

def cube(x):
    return x*x*x

def sum_cube(n):
    return summation(n,cube)

def double(x):
    return x*2

def sum_double(n):
    return summation(n,double)

print(sum_cube(3))
print(sum_double(3))



def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess +1

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y) < tolerance

def golden_close(guess):
    return approx_eq(guess*guess,guess+1)

print(improve(golden_update,golden_close))

