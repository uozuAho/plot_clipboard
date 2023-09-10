""" Read markdown tables from stdin and plot them """

import sys
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    headings, data_strs = read_raw_columns()
    x = parse_date_column(data_strs[0])
    float_data = []
    for col in data_strs:
        try:
            float_data.append(parse_float_column(col))
        except ValueError:
            pass

    # print(headings)
    # for i in range(len(float_data[0])):
    #     print([x[i] for x in float_data])

    for col in float_data:
        plt.plot(x, col)
    plt.legend(headings[1:])
    plt.show()


def read_raw_columns():
    """ Read all column data as strings

        Returns: str[], str[]: column_headings, column_values
    """
    column_headings = []
    column_value_strs = []
    for line in sys.stdin:
        print(line)
        if not column_headings:
            column_headings = [x.strip() for x in line.split('|')]
            column_value_strs = [[] for _ in column_headings]
            continue
        if line.startswith('----'):
            continue
        for i, x in enumerate(line.split('|')):
            column_value_strs[i].append(x.strip())
    return column_headings, column_value_strs


def parse_date_column(col):
    return [datetime.strptime(x, '%Y-%m-%d') for x in col]


def parse_float_column(col):
    return [float(x) if x else None for x in col]


if __name__ == '__main__':
    main()
