""" Read markdown tables from stdin and plot them """

import sys
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    headings, data_strs = read_raw_columns()
    # assume first column is date, x axis
    x = parse_date_column(data_strs[0])
    float_data = []
    text_data = []
    for col in data_strs[1:]:
        try:
            float_data.append(parse_float_column(col))
        except ValueError:
            text_data.append(col)

    for col in float_data:
        plt.plot(x, col)
    plt.legend(headings[1:])
    _, ymax = yminmax(float_data)

    # Add notes. assume one note column, if any
    plt.ylim(-2, ymax * 1.1)
    text_ys = [-.5, -1, -1.5, -2]
    text_y_idx = 0
    for xpos, txt in zip(x, text_data[0]):
        if txt:
            text_y_idx = (text_y_idx + 1) % len(text_ys)
            plt.annotate(txt, xy=(xpos, 0), xytext=(xpos, text_ys[text_y_idx]),
                         rotation=45, ha='center',
                         arrowprops=dict(arrowstyle='->'))
    plt.show()


def read_raw_columns():
    """ Read all column data as strings

        Returns: str[], str[]: column_headings, column_values
    """
    column_headings = []
    column_value_strs = []
    for line in sys.stdin:
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
    return [float(x) if not isblank(x) else None for x in col]


def isblank(x):
    return x is None or x == '' or x == '?'


def yminmax(float_data):
    min_val = float('inf')
    max_val = float('-inf')
    for col in float_data:
        for val in col:
            if val is not None:
                min_val = min(min_val, val)
                max_val = max(max_val, val)
    return min_val, max_val


if __name__ == '__main__':
    main()
