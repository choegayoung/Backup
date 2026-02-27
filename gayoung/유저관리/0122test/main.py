import argparse
from method import list, add, select, update, quit, zagaip

commands= [
    {"command": "list", "argument": [], "method": list},
    {"command": "add", "argument": ['name','email','pwd','gender'], "method": add},
    {"command": "select", "argument": ['no'], "method": select},
    {"command": "update", "argument": ['no','key','value'], "method": update},
    {"command": "quit", "argument": ['no'], "method": quit},
    {"command": "zagaip", "argument": ['no'], "method": zagaip},
]

DESC = "2팀짱짱맨뿡뿡ㅋ"
def checkCLI(args):
    for cmd in commands:
        if cmd["command"] == args.command:
            if cmd["method"] == None :
                print('없어용')
            else : cmd["method"](args)
            break
    print('종료')

def run():
    parser = argparse.ArgumentParser(description=DESC)
    subparser = parser.add_subparsers(dest="command")
    for cmd in commands:
        name= cmd["command"]
        arguments = cmd['argument']
        add_parser = subparser.add_parser(name)
        for arg in arguments:
            add_parser.add_argument(arg)

    checkCLI(parser.parse_args())

if __name__ == '__main__':
    run()
