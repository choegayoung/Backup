import argparse
from method import empty, userEdit, boardEdit, userList,boardList, userAdd, boardAdd, userDetail,boardDetail, userDelete, boardDelete

DESC = "CLI Program"
commands = [
  {"command":"userList", "arguments": [], "method": userList},
  {"command":"boardList", "arguments": [], "method": boardList},
  {"command":"userAdd", "arguments": ['name','email','password','gender'], "method": userAdd},
  {"command":"boardAdd", "arguments": ['title','content','user_no'], "method": boardAdd},
  {"command":"userDetail", "arguments": ['no'], "method": userDetail},
  {"command":"boardDetail", "arguments": ['no'], "method": boardDetail},
  {"command":"userEdit", "arguments": ['no','key','value'], "method": userEdit},
  {"command":"boardEdit", "arguments": ['no','key','value'], "method": boardEdit},
  {"command":"userDelete", "arguments": ['no'], "method": userDelete},
  {"command":"boardDelete", "arguments": ['no'], "method": boardDelete},
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
