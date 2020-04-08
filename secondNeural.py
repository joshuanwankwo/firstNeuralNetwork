print("Please add two inputs!")


import random
import math


def sigmoid(x):
    sig = 1/(1 + math.exp(-x))
    return sig

def main():
    x1 = int(input())

    x2 = int(input())

    w1 = random.randint(0,9)

    w2 = random.randint(0,9)

    w3 = random.randint(0,9)

    net1 = x1 * w1
    net2 = x1 * w2
    net3 = x1 * w3


    w4 = random.randint(0,9)

    w5 = random.randint(0,9)

    w6 = random.randint(0,9)

    net4 = x2 * w4
    net5 = x2 * w5
    net6 = x2 * w6

    f1 = net1 + net4
    firstNeron = sigmoid(f1)
    print("the first neuron is " + str(firstNeron))

    f2 = net2 + net5
    secoundNeuron = sigmoid(f2)
    print("the secound neuron is " + str(secoundNeuron)) 

    f3 = net3 + net6
    thirdNeuron = sigmoid(f3)
    print("the third neuron is " + str(thirdNeuron))

    w7 = random.randint(0,9)

    w8 = random.randint(0,9)

    w9 = random.randint(0,9)

    net7 = firstNeron * w7
    net8 = firstNeron * w8
    net9 = firstNeron * w9


    w10 = random.randint(0,9)

    w11 = random.randint(0,9)

    w12 = random.randint(0,9)

    net10 = secoundNeuron * w10
    net11 = secoundNeuron * w11
    net12 = secoundNeuron * w12


    w13 = random.randint(0,9)

    w14 = random.randint(0,9)

    w15 = random.randint(0,9)

    net13 = thirdNeuron * w13
    net14 = thirdNeuron * w14
    net15 = thirdNeuron * w15

    f4 = net7 + net10 + net13
    fourthNeuron = sigmoid(f4)
    print("the fourth Neuron is " + str(fourthNeuron))

    f5 = net8 + net11 + net14
    fifthNeuron = sigmoid(f5)
    print("ther fifth Neuron is " + str(fifthNeuron))

    f6 = net9 + net12 + net15
    sixthNeuron = sigmoid(f6)
    print("the sixth Neuron is " + str(sixthNeuron))

    

    w16 = random.randint(0,9)

    w17 = random.randint(0,9)

    w18 = random.randint(0,9)

    net16 = fourthNeuron * w16
    net17 = fourthNeuron * w17
    net18 = fourthNeuron * w18


    w19 = random.randint(0,9)

    w20 = random.randint(0,9)

    w21 = random.randint(0,9)

    net19 = fifthNeuron * w19
    net20 = fifthNeuron * w20
    net21 = fifthNeuron * w21


    w22 = random.randint(0,9)

    w23 = random.randint(0,9)

    w24 = random.randint(0,9)

    net22 = sixthNeuron * w22
    net23 = sixthNeuron * w23
    net24 = sixthNeuron * w24


    f7 = net16 + net19 + net22
    seventhNeuron = sigmoid(f7)
    print("the seventh Neuron is " + str(seventhNeuron))

    f8 = net17 + net20 + net23
    eightNeuron = sigmoid(f8)
    print("the eight Neuron is " + str(eightNeuron))

    f9 = net18 + net21 + net24
    ninethNeuron = sigmoid(f9)
    print("the nineth Neuron is " + str(ninethNeuron))


    w25 = random.randint(0,9)

    w26 = random.randint(0,9)


    w27 = random.randint(0,9)

    w28 = random.randint(0,9)


    w29 = random.randint(0,9)

    w30 = random.randint(0,9)

    net25 = seventhNeuron * w25
    net26 = seventhNeuron * w26

    net27 = eightNeuron * w27
    net28 = eightNeuron * w28

    net29 = ninethNeuron * w29
    net30 = ninethNeuron * w30

    f10 = net27 + net27 + net29
    tenthNeuron = sigmoid(f10)
    print("the tenth Neuron is " + str(tenthNeuron))

    f11 = net26 + net28 + net30
    eleventhNeuron = sigmoid(f11)
    print("the eleventh Neuron is " + str(eleventhNeuron))

    w31 = random.randint(0,9)

    w32 = random.randint(0,9)

    net31 = tenthNeuron * w31

    net32 = eleventhNeuron * 32

    f12 = net31 + net32
    twelvethNeuron = sigmoid(f12)
    print("the twelveth Neuron which is also the final output is " + str(twelvethNeuron))



main()