import argparse
from method import empty, list, add, update, remove

DESC = "CLI Program"
commands = [
  {"command":"t2_read", "arguments": [], "method": list},
  {"command":"t2_create", "arguments": ["content"], "method": add},
  {"command":"t2_update", "arguments": ["id", "content"], "method": update},
  {"command":"t2_delete", "arguments": ["id"], "method": remove}
]

def checkCLI(args):
  for cmd in commands:
    if args.command == cmd["command"]:
      if cmd["method"] == None:
        empty()
      else:
        cmd["method"](args)
      break
  print("종료")

def run():
  parser = argparse.ArgumentParser(description=DESC)
  subparsers = parser.add_subparsers(dest="command")

  for cmd in commands:
    name = cmd["command"]
    arguments = cmd["arguments"]
    add_parser = subparsers.add_parser(name)
    for arg in arguments:
      add_parser.add_argument(arg)

  checkCLI(parser.parse_args())

if __name__ == "__main__":
  run()