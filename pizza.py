# Program to compute the cost per square inch of a circular pizza
# given the diameter and price

# N/B: radius = diameter/2

from math import *

def pizzaArea(radius):

    area = pi * (radius ** 2)

    return area

def main():
    print("This program computes the cost per square inch of a")
    print("circular pizza\n")

    

    d = float(input("Enter the diameter of the pizza: "))
    p = float(input("Enter the price of the pizza: "))

    r = d / 2

    a = pizzaArea(r)

    c = p / a

    print("The area of the pizza is {0}".format(a))
    print("The cost per square inch of the pizza is {0:0.2f} ".format(c))
    

main()
