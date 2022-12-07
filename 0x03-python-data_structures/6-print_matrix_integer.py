#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(0, len(i)):
            print("{:d}".format(i[j]), end="")
            if j != len(i) - 1:
                print(" ", end="")

        print("")
