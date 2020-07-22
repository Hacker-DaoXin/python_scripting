# coding:utf-8
import os
def remove_dup(readDir,writeDir):
    outfile = open(writeDir, "w")
    f = open(readDir, "r")

    lines_seen = set()  # Build an unordered collection of unique elements.

    for line in f:
        line = line.strip('\n')
        if line not in lines_seen:
            outfile.write(line + '\n')
            lines_seen.add(line)
            print("Finished removing duplicate parameters in the text, \n"
                  "new file at :{}"%os.path(writeDir))

