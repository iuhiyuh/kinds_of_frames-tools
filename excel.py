# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
import operator
import sys

"""
python excel.py "file path" "target file path"
"""
def load_csv(csv_path):
    data = pd.read_csv(csv_path,encoding="utf_8_sig")
    return data


if __name__ == '__main__':
    dir_path = sys.argv[1]
    dst_path = sys.argv[2]
    pd.set_option('mode.chained_assignment', None)
    csv = load_csv(dir_path)
    newcsv = []
    last_row = pd.Series(csv.loc[0, :].shape)
    j = 0
    for i in range(csv.shape[0]):
        row = csv.loc[i, :]
        row_no_label = row[:3]
        label = row[3]
        if j == 0:
            last_row = row
            newcsv.append(last_row)
        else:
            if all(operator.eq(row_no_label.get_values(), last_row[0:3].get_values())):
                newcsv[-1].iloc[3] = '精彩配合得分'
            else:
                last_row = row
                newcsv.append(last_row)
                pass
            pass
        j += 1

    newcsv = pd.DataFrame(newcsv)
    newcsv.to_csv(dst_path, encoding="utf_8_sig", index=False)
    pass
