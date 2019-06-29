# coding: UTF-8

import input
import request

# 入力取得
args = sys.argv
f_path = args[0]

# csvファイル取得
print('read_csv')
csv_f = input.read_csv(f_path)
print('read_csv fin')

# リクエスト
print('request')
res = request.multi_url_get(csv_f)
print('request fin')
