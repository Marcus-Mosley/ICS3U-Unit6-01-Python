#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on November 2020
# This program finds the average of a random array of 10 numbers

import random


def main():
    # This function finds the average of a random array of 10 numbers

    number_array = []

    # Input
    for loop_counter in range(0, 10):
        number = random.randint(1, 100)
        number_array.append(number)
        print("The random number is: {}".format(number))
    print(" ")

    # Process & Output
    average = sum(number_array) / 10
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
