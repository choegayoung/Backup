print("파이썬")

import argparse
from cmd import add ,list

## 파이썬에서는 from 파일명 먼저쓰고, import 함수명 쓰기

parser = argparse.ArgumentParser(description="CLI 프로그램")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="메모추가")
add_parser.add_argument("a", help="메모 내용")
add_parser.add_argument("b", help="메모 내용")

add_parser = subparsers.add_parser("list", help="메모추가")

args = parser.parse_args()


if args.command == "add" :
    add(args.a, args.b)
elif args.command == "list" :
    list()

## 파이썬에서는 콜백함수 사용 X