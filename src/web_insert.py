"""
重构后的爬虫主模块。输出与数据文件会统一放到项目的 data/ 和 output/ 目录下。
"""
from pathlib import Path
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url_douban = 'https://movie.douban.com/top250'  # 这里输入你想爬取的网页
url_book = 'https://books.toscrape.com/'        # 测试用的网页

# 国外书单网址
def spider_book(url, out_path: Path = None):
    out_path = out_path or (DATA_DIR / 'books.txt')
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            articles = soup.find_all('article', class_='product_pod')
            with open(out_path, 'w', encoding='utf-8') as file:
                for article in articles:
                    h3 = article.find('h3')
                    a_tag = h3.find('a')
                    title = a_tag.get('title') or a_tag.get_text(strip=True)
                    p = article.find('p', class_='price_color')
                    price = p.get_text() if p else ''
                    line = f"书名: {title:<100}价格:{price:<10}\n"
                    file.write(line)
                    print(line, end='')
        print("---------------------国外书单爬取成功，内容已保存到 %s ---------------------" % out_path)
    except Exception as e:
        print("测试失败，错误信息：", e)

# 用于爬取豆瓣
def spider_douban(url, out_path: Path = None):
    out_path = out_path or (DATA_DIR / 'douban.txt')
    idx = 1
    with open(out_path, 'w', encoding='utf-8') as file:
        for start_num in range(0, 250, 25):
            new_url = f"{url}?start={start_num}&filter="
            response = requests.get(new_url, headers=headers)
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                for item in soup.find_all('div', class_='item'):
                    title_tag = item.find('span', class_='title')
                    title = title_tag.get_text() if title_tag else ''
                    rating_tag = item.find('span', class_='rating_num')
                    rating = rating_tag.get_text() if rating_tag else ''
                    line = f"{idx:<3}. 电影: {title:<30}评分: {rating:<5}\n"
                    file.write(line)
                    print(line, end='')
                    idx += 1
            else:
                print("无法访问该网页, 状态码: ", response.status_code)
    print("---------------------豆瓣Top250爬取成功，内容已成功保存到 %s ---------------------" % out_path)


if __name__ == '__main__':
    print("src.web_insert: 开始测试爬虫功能...")
    spider_book(url_book)
    spider_douban(url_douban)
