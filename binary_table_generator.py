#!/usr/bin/env python
"""Binary Table Generator: A program that generates a csv for a truth table for a given number of columns"""

__author__ = "Nick Dawson"
__copyright__ = "Copyright 2018, Nick Dawson"
__version__ = "1.0.0"

import csv


def binary_table(columns):
    if columns > 19:
        raise OverflowError('CSV cannot be more than 1,000,000 rows, maximum amount of columns is 19')
    elif columns <= 0:
        raise ValueError('Cannot generate a table with negative or zero columns, please use a number greater than 0')
    length = int((2 ** columns) / 2)
    table = []
    file_name = 'BinaryTable-' + str(columns) + 'Columns.csv'
    header = []
    for x in range(columns):
        header.append('N-' + str(x + 1))
    for x in range(columns):
        times = int(2 ** (x + 1) / 2)
        res = ''
        for y in range(int(length / times)):
            res = res + (times * '0')
            res = res + (times * '1')
        table.append(list(res))

    table = list(reversed(table))

    with open(file_name, 'w', newline='') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow(header)
        for column in zip(*table):
            file_writer.writerow(column)
