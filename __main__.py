import os
import sys

#setting up the parser
args = sys.argv
print args
args = args[1:len(args)]
print args
cwd = os.getcwd()

override = False

def make_gitignore(args):
    text=''
    for arg in args:
        if(arg != '-o'):
            text += arg +'\n'

    file = open(cwd+'/.gitignore', 'w')
    file.write(text)
    file.close()


if not os.path.isfile(cwd+'/.gitignore'):
    make_gitignore(args)
else:
    if(args[len(args)-1] == '-o'):
        make_gitignore(args)
    else:
        print args[len(args)-1]
        print ".gitignore already exists, add -o flag, in the end to override the previous one"
