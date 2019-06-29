# coding: UTF-8

import requests
import traceback
import csv
import sys
import time
import pandas as pd
from bs4 import BeautifulSoup

# 証明書 うまく動作しなかったため未使用
CART_PATH = ''
# 保存先
SAVE_PREFIX = '/var/www/PythonScraping/result/'
# PC SP 出しわけの為のUA
SP_HEADER = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'}
PC_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

def request(url, headers):
    print(url)
    response = requests.get(url, headers=headers, verify=False)
    return response

# リクエスト実行
def download_html(url, headers):
    response = request(url, headers)
    if response.status_code == 200:
        return response.content
    else:
        print('ダウンロードに失敗しました\nステータスコード：', response.status_code)
        sys.exit()

# ファイルに保存
def save_file(data, file_name):
    try:
        with open(file_name, 'wb') as f:
            f.write(data)
    except:
        print('データの保存に失敗しました')
        traceback.print_exc()

def get_headers(ua):
    if ua == 'pc':
        headers = PC_HEADER
    else:
        headers = SP_HEADER

    return headers

# csvからurlを取得しステータスコードを保存する
def get_status(csv_file_path):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)

        datas = list()
        for row in reader:
            url = row[0]
            ua = row[1]

            headers = get_headers(ua)
            res = request(url, headers)
            status = res.status_code
            datas.append([url, ua, status])
            time.sleep(0.5)

        df = pd.DataFrame(
            datas,
            columns=["url", "UA", "status"]
            )
        df.to_csv(SAVE_PREFIX + "status.csv")

# csvからurlを取得しステータスコードを保存する
def get_884(csv_file_path):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)

        datas = list()
        for row in reader:
            url = row[0]
            ua = row[1]

            headers = get_headers(ua)
            res = request(url, headers)
            if res.status_code != 200:
                print('ダウンロードに失敗しました\nステータスコード：', res.status_code)
                sys.exit()
                 
            status = res.status_code
            soup = BeautifulSoup(res.text, 'lxml')
            vars(breadcrumb = soup.find('.bread_area ol li:nth-child(2)'))
            sys.exit()
            breadcrumb = soup.find('.bread_area ol li:nth-child(2)').text
            h1 = soup.find('h1').text

            datas.append([url, ua, status, breadcrumb, h1])
            time.sleep(0.5)

        df = pd.DataFrame(
            datas,
            columns=["url", "UA", "status", "breadcrunb", "h1"]
            )
        df.to_csv(SAVE_PREFIX + "884.csv")



args = sys.argv
# ステータスコード
# get_status(args[1])
get_884(args[1])

