import unittest

def fibo(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1

    a,b = 0,1
    for i in range(2, n+1):
        a,b = b, a+b
        return b
    
class hasonlit(unittest.TestCase):
    def test_two_positive(self):
        fgv = fibo(0.1)
        print(fgv)
    def test_two(self):
        fgv = fibo(-2)
        print(fgv)
    def test_three(self):
        fgv = fibo(-3)
        print(fgv)

    
unittest.main()
    