#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

NUMBER_TIMES = {'A':1,'B':2,'C':3,'D':1,'E':2,'F':3,'G':1,'H':2,'I':3,'J':1,'K':2,'L':3,'M':1,'N':2,'O':3,
                'P': 1, 'Q': 2, 'R': 3,'S':4,'T':1,'U':2,'V':3,'W':1,'X':2,'Y':3,'Z':4,}

filename = "task1-test-input.txt"
resultfilename = "task1-test-output.txt"

def readfile(filename):
    with open(filename,'r') as f:
        data = [line for line in f.readlines()]
        data = [x.strip('\n') for x in data]
        del data[0]
        return data

def TypingTime(data):
    times = []
    for i in range(len(data)):
        datalist = list(data[i])
        time = 0
        for k in range(len(datalist)):
            time += NUMBER_TIMES[datalist[k]]
        times.append(time)
    return times

def writefile(data,writefilename):
    with open(writefilename,'w') as f:
        for index, num in enumerate(data):
            f.write('Case #%d: %d\r\n' % (index + 1, num))


if __name__ == '__main__':
    writefile(TypingTime(readfile(filename)),resultfilename)
