import argparse
from cmd import add, list, remove

parser = argparse.ArgumentParser(description="CLI 프로그램")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="메모 추가")
add_parser.add_argument("word", help="메모 내용")

add_parser = subparsers.add_parser("list", help="메모 리스트")

add_parser = subparsers.add_parser("remove", help="단어 삭제")
add_parser.add_argument("word", help="삭제할 단어")

args = parser.parse_args()

if args.command == "add" :
    add(args.word)
elif args.command == "list" :
    list()

if args.command == "remove" :
    remove(args.word)
elif args.command == "list" :
    list()
