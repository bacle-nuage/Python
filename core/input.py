# coding: UTF-8

import csv

# csv読み込み
def read_csv(path):
    csv_file = open("./TEST_STOCK.csv", "r", encoding="ms932", errors="", newline="")
    # 辞書形式
    f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return f

# 保存
def save(data, file_name):
    try:
        with open(file_name, 'wb') as f:
            f.write(data)
    except:
        print('データの保存に失敗しました')
        traceback.print_exc()
