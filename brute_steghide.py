#!/usr/bin/env python
import sys
import commands

if __name__ == '__main__':
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        wordlist = sys.argv[2]
    else:
        print "Usage: {0} <filename> <wordlist>".format(sys.argv[0])
        sys.exit()

    f = open(wordlist, 'r')
    lines = f.readlines();
    found = False
    cont = 1
    for line in lines:
        if line.strip().isalnum():
            output = commands.getoutput("steghide extract -sf " + filename.strip() + " -p " + line.strip())
            if output.find("steghide") == -1:
                print "Password found: ", line 
                found = True
                break

    if not found:
        print "Password not found"
