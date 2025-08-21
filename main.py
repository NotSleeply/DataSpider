#!/usr/bin/env python3
"""
main.py - 简单命令行入口，用于运行爬虫并将结果保存到 data/ 或自定义路径。
Windows (PowerShell) 使用示例:
  python .\main.py --books
  python .\main.py --douban
  python .\main.py --both --books-out data\my_books.txt --douban-out data\my_douban.txt
"""
from pathlib import Path
import argparse
import sys

from src.web_insert import (
    BASE_DIR,
    DATA_DIR,
    OUTPUT_DIR,
    spider_book,
    spider_douban,
    url_book,
    url_douban,
)


def _resolve_out(path_str: str, default: Path) -> Path:
    if not path_str:
        return default
    p = Path(path_str)
    return p if p.is_absolute() else (BASE_DIR / p)


def main(argv=None):
    parser = argparse.ArgumentParser(description='DataSpider 主入口 — 运行爬虫并保存结果')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--books', action='store_true', help='仅抓取书籍列表')
    group.add_argument('--douban', action='store_true', help='仅抓取豆瓣 Top250')
    group.add_argument('--both', action='store_true', help='同时抓取书籍与豆瓣')

    parser.add_argument('--books-out', type=str, help='书籍输出文件（相对 BASE_DIR 或绝对路径）')
    parser.add_argument('--douban-out', type=str, help='豆瓣输出文件（相对 BASE_DIR 或绝对路径）')

    args = parser.parse_args(argv)

    # 默认行为：如果未传任何标志，则执行 both
    run_books = args.books or args.both or (not (args.books or args.douban or args.both))
    run_douban = args.douban or args.both or (not (args.books or args.douban or args.both))

    books_out = _resolve_out(args.books_out, DATA_DIR / 'books.txt')
    douban_out = _resolve_out(args.douban_out, DATA_DIR / 'douban.txt')

    print(f'BASE_DIR: {BASE_DIR}')
    print(f'输出 - 书籍: {books_out}  豆瓣: {douban_out}')

    try:
        if run_books:
            print('开始抓取书籍...')
            books_out.parent.mkdir(parents=True, exist_ok=True)
            spider_book(url_book, out_path=books_out)

        if run_douban:
            print('开始抓取豆瓣 Top250...')
            douban_out.parent.mkdir(parents=True, exist_ok=True)
            spider_douban(url_douban, out_path=douban_out)

        print('完成。')
    except KeyboardInterrupt:
        print('\n已取消（KeyboardInterrupt）')
        sys.exit(1)
    except Exception as e:
        print('运行出现错误：', e)
        sys.exit(2)


if __name__ == '__main__':
    main()
