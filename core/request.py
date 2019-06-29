# coding: UTF-8

import requests
from bs4 import BeautifulSoup

# UserAgent
SP_HEADER = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'}
PC_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

def get_headers(ua):
    if ua == 'pc' | ua == 'PC':
        headers = PC_HEADER
    else:
        headers = SP_HEADER

    return headers

def check_err(res):
    if res.status_code != 200:
        print('ダウンロードに失敗しました\nステータスコード：', res.status_code)
        sys.exit()

def bs(html):
    return BeautifulSoup(html, 'lxml')

def get(csv_f):
    url = csv_f['url']
    ua = csv_f['ua']
    headers = get_headers(ua)
    res = requests.get(url, headers=headers, verify=False)
    if res.status_code != 200:
        print('ダウンロードに失敗しました\nステータスコード：', res.status_code)
        sys.exit()
    print(res.status_code)

    return bs(res.text)

def multi_url_get(csv_f):
    responses = list()
    for f in csv_f:
        url = f['url']
        ua = f['ua']
        headers = get_headers(ua)
        res = requests.get(url, headers=headers, verify=False)
        if res.status_code != 200:
            print('ダウンロードに失敗しました\nステータスコード：', res.status_code)
            sys.exit()
        responses.append(bs(res.text))
        print('url' + url + 'status : ' + res.status_code)

    return responses
