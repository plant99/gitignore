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
#Exit if multiple flags are passed
count=0
for arg in args:
    if(arg[0] == '-'):
        count+=1

if(count > 1):
    print "Pass valid parameters!"
    sys.exit()

def make_gitignore(args, flag):
    text=''
    for arg in args:
        if(arg != '-o' and arg != '-a'):
            text += arg +'\n'

    if( flag == 'w'):
        file = open(cwd+'/.gitignore', 'w')
    else:
        file = open(cwd+'/.gitignore', 'a')
    file.write(text)
    file.close()




if not os.path.isfile(cwd+'/.gitignore'):
    make_gitignore(args, 'w')
else:
    if(args[len(args)-1] == "-o"):
        make_gitignore(args, 'w')
    elif(args[len(args)-1] == '-a'):
        make_gitignore(args, 'a')
    else:
        print ".gitignore already exists, add -o flag, in the end to overwrite the previous one, -a to append the lines to .gitignore"
