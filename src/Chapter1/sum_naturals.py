from doctest import testmod

def sum_naturals(n):
    """
    返回自然数之和
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total,k = 0,1
    while k<=n:
        total,k = total+k,k+1
    return total

print(testmod())