"""
Project Name: Fast Exponentiation
Programmer: Michaela Pierce
Date: 12/04/22
UNCW, CSC 592 - Introduction to Cryptography
"""

def expMod(x, e, n):
    binary=format(e,'b')
    e= binary[1:]
    y = x
    for i in range(len(e)):
        y = y * y % n
        if e[i] == '1':
            y = (y * x) % n
    return y

if __name__ == '__main__':
   #x = (int(input("please enter value for x : ")))
   #e = (int(input("please enter value for e : ")))
   #n = (int(input("please enter value for n : ")))
   #print(" x is : ", x, "\n","e is : ", e, "\n","n is : ",n, "\n", "The result is : ", expMod(x,e,n))
   print(expMod(20,30,24))

