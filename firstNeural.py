print("STILL CONNECTED")


import random
import math


def sigmoid(x):
    sig = 1/(1 + math.exp(-x))
    return sig


def main():
    x1 = int(input())

    x2 = int(input())


    w1 = random.randint(0, 9)
    
    w2 = random.randint(0, 9)

    deltal1 = x1 * w1
    deltal2 = x2 * w2

    z1 = deltal1 + deltal2

    print(z1)
    print(sigmoid(z1))




    f1 = sigmoid(z1)

    w3 = random.randint(0, 9)

    w4 = random.randint(0, 9)

    deltal3 = x1 * w3
    deltal4 = x2 * w4

    z2 = deltal3 + deltal4

    f2 = sigmoid(z2)
    print(sigmoid(f2))




    w5 = random.randint(0, 9)

    w6 = random.randint(0, 9)

    deltal5 = f1 * w5

    deltal6 = f2 * w6

    z3 = deltal5 + deltal6
    f3 = (sigmoid(z3))
    print(sigmoid(z3))


    w7 = random.randint(0, 9)

    w8 = random.randint(0, 9)

    deltal7 = f1 * w7

    deltal8 = f2 * w8

    z4 = deltal7 + deltal8
    f4 = sigmoid(z4)
    print(sigmoid(z3))


    w9 = random.randint(0, 9)

    w10 = random.randint(0, 9)

    deltal9 = f3 * w9

    deltal10 = f4 * w10

    z5 = deltal9 + deltal10
    f5 = sigmoid(z5)
    print(f5)




main()