import requests
import traceback
import csv
import sys
import time

# 証明書 うまく動作しなかったため未使用
CART_PATH = ''
# 保存先
SAVE_PREFIX = '/var/www/PythonScraping/html/'
# PC SP 出しわけの為のUA
SP_HEADER = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'}
PC_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

# リクエスト実行
def download_data(url, headers):
    print(url)
    response = requests.get(url, headers=headers, verify=False)
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

# 新旧URL判断
def get_url(row, gen):
    if gen == 'new':
        path = row[2]
    else:
        path = row[1]

    return row[0] + path

def get_ua(ua):
    if ua == 'pc':
        headers = PC_HEADER
    else:
        headers = SP_HEADER

    return headers

# csvからurlを取得しhtmlを保存する
def get_html(csv_file_path, gen):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            url = get_url(row, gen)
            headers = get_ua(row[4])

            html = download_data(url, headers)
            save_file(html, SAVE_PREFIX + row[3])
            time.sleep(1)

args = sys.argv
get_html(args[1], args[2])

