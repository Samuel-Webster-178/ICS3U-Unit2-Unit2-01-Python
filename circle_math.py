#!/usr/bin/env python3

# Created by Samuel Webster
# Created on February 2022
# This program calculates the area and circumference of a circle
# with radius 15mm

import math


def main():
    # I calculate and print the circumference and area
    print("If a circle has a radius of 10 m: ")
    print("Area is {} m².".format(math.pi * 15**2))
    print("Circumference is {} m.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
