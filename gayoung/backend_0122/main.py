import argparse
from method import select, insert, update, delete

DESC = "CLI Program"
commands = [
  {"command":"v", "arguments": [], "method": select},
  {"command":"a", "arguments": ["word"], "method": insert},
  {"command":"u", "arguments": ["id", "word"], "method": update},
  {"command":"d", "arguments": ["id"], "method": delete}
]
def checkCLI(args):
  for cmd in commands:
    if args.command == cmd["command"]:
      if cmd["method"] == None:
        print("정의 되어 있지 않습니다.")
      else:
        cmd["method"](args)
      break 
  print("종료")


def run():  
  parser = argparse.ArgumentParser(description=DESC)
  subparsers = parser.add_subparsers(dest="command")

  for cmd in commands:
    add_parser = subparsers.add_parser(cmd["command"])
    for arg in cmd["arguments"]:
      add_parser.add_argument(arg)
  
  checkCLI(parser.parse_args())

if __name__ == "__main__":
  run()