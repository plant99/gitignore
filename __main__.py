import os
import sys

#setting up the parser
args = sys.argv
args = args[1:len(args)]
cwd = os.getcwd()

override = False

if( args[0] == '-h'):
    print ''
    print "RUN gitignore <REGEX> <REGEX> .... to write a .gitgnore"
    print ''
    print "If a .gitignore exists, append '-o' to the end to overwrite it"
    print ''
    sys.exit()

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
        print ".gitignore already exists, add -o flag, in the end to overwrite the previous one"
