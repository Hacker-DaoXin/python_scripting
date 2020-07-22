# -*- coding: utf-8 -*-

import requests
import urllib3
import requests
from bs4 import BeautifulSoup



def get_code_status(urls_file):
    """
    检测urls状态码
    :param urls_file: urls文件
    :return: 状态码
    allow_redirects: 拒绝默认的301/302重定向从而可以通过 html.headers[‘Location’] 拿到重定向的 URL。
    verify: 取消证书认证
    """


    request_test = open("request_test.txt", 'w')

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
    }
    with open(urls_file, 'r', encoding='utf-8') as f:
        urls_data = f.readlines()
        for url in urls_data:
            url = url.strip('\n')
            url2 = open("lujing.txt", 'r')
            second = url2.readlines()
            disable_warnings()
        for u in second:
            u = u.strip('\n')
            finalurl=url+u
            try:
                res = requests.get(
                    finalurl, headers=header, verify=False, allow_redirects=False
                )

            except Exception as error:
                print(error)
            code = res.status_code
            res.encoding= 'utf-8'
            soup=BeautifulSoup(res.text,'lxml')
            if code != 200:
                try:
                    print('状态码 {}:{}'.format(code, finalurl))
                    request_test.write('状态码 {}:{}:{}'.format(code, finalurl,soup.title.text)+'\n')
                except AttributeError:
                    print("No title")
            elif code == 200:
                try:
                    print('状态码 {}:{}'.format(code, finalurl))
                    request_test.write('状态码 {}:{}:{}'.format(code, finalurl,soup.title.text) + '\n')
                except AttributeError:
                    print("No title")

    return code



def disable_warnings():
    """
    解除去掉证书后总是抛出异常告警
    """
    urllib3.disable_warnings()


if __name__ == '__main__':
    get_code_status('/Users/chichizhu/Desktop/DXY/cms.txt')


