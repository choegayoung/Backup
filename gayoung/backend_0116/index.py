import argparse

from test import list, insert, update, remove

command =[
    {"command":"list", "argument": [], "method": list},
    {"command":"insert", "argument": ["word"], "method": insert},
    {"command":"update", "argument": ["id", "word"], "method": update},
    {"command":"remove", "argument": ["id"], "method": remove}
]

parser = argparse.ArgumentParser(description="CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser ("list")
add_parser = subparsers.add_parser ("insert")
add_parser.add_argument ("word")
add_parser = subparsers.add_parser ("update")
add_parser.add_argument ("id")
add_parser.add_argument ("word")
add_parser = subparsers.add_parser ("remove")
add_parser.add_argument ("id")


for cmd in command:
    add_parser = subparsers.add_parser(cmd["command"])
    for arg in cmd["argument"]:
        add_parser.add_argument (arg)

args = parser.parse_args()

if args.command == "list" : list()
if args.command == "insert" : insert(args.word)
if args.command == "update" : update(args.id, args.word)
if args.command == "remove" : remove(args.id)