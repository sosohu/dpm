import os
import requests
from bs4 import BeautifulSoup
import argparse
import ast
import atexit
import multiprocessing
import sys

parser = argparse.ArgumentParser(description='Spider for jiandan.net')
parser.add_argument('--page', dest='page', action='store', default=1, type=int, help='max page number')
parser.add_argument('--dir', dest='dir', action='store', default='images', help='the dir where the image save')
args = parser.parse_args()

page = args.page
_dir = args.dir
if not os.path.exists(_dir):
    os.mkdir(_dir)

headers = {}
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Referer'] = 'https://digicol.dpm.org.cn/list?category=17'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Accept-Language'] = 'en'
headers['Cache-Control'] = 'max-age=0'
headers['Connection'] = 'keep-alive'
headers['Upgrade-Insecure-Requests'] = '1'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
headers['Host'] = 'digicol.dpm.org.cn'
headers['Sec-Fetch-Dest'] = 'document'
headers['Sec-Fetch-Mode'] = 'navigate'
headers['Sec-Fetch-Site'] = 'same-origin'
headers['Sec-Fetch-User'] = '?1'
headers['Cookie'] = 'UM_distinctid=171e276361721d-07040da54deddc-c373667-1fa400-171e2763618c4a; cn_1261553859_dplus=%7B%22distinct_id%22%3A%20%22171e276361721d-07040da54deddc-c373667-1fa400-171e2763618c4a%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201588642343%2C%22initial_view_time%22%3A%20%221588637302%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.dpm.org.cn%2FHome.html%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.dpm.org.cn%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201588642343%7D; CNZZDATA1277672184=240792894-1588641413-%7C1588641413; szwwcookietip=true; SESSION=ODNkMGViODktZjJjNS00MzEyLWI4ZTItMmFlMDMwZTQyOGQz; cn_1277672184_dplus=%7B%22distinct_id%22%3A%20%22171e276361721d-07040da54deddc-c373667-1fa400-171e2763618c4a%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201588646312%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201588646312%2C%22initial_view_time%22%3A%20%221588641413%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D'

image_cache = set()

if os.path.exists(".cache"):
    with open('.cache', 'r') as f:
        image_cache = ast.literal_eval(f.read(-1))


@atexit.register
def hook():
    with open('.cache', 'w+') as f:
        f.write(str(image_cache))


index = len(image_cache)


def save_jpg(res_url):
    global index
    page_response = requests.get(res_url, headers=headers)
    if page_response.status_code != 200:
        print(page_response.status_code)
        sys.exit(0)

    html = BeautifulSoup(page_response.content, features="html.parser")
    print(page_response.content)
    #print(html)
    for link in html.find_all('div', {'class': 'pic'}):
        print(link)
        # if link.get('href') not in image_cache:
        #     with open(
        #             '{}/{}.{}'.format(_dir, index, link.get('href')[len(link.get('href')) - 3: len(link.get('href'))]),
        #             'wb') as jpg:
        #         jpg.write(requests.get("http:" + link.get('href')).content)
        #     image_cache.add(link.get('href'))
        #     print("Fetching %s th data" % index)
        #     index += 1


if __name__ == '__main__':
    urlTemplate = 'https://digicol.dpm.org.cn/list?page={page}&category=17'
    for i in range(1, page + 1):
        url = urlTemplate.format(page = i)
        save_jpg(url)