#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Janelle Kuhns"

import sys


def is_nested(line):
    stack = []
    for l in line:
        if "(" in l:
            stack.append('(')
        else:
            stack.pop()
            if '{' in l:
                stack.append('{')
            else:
                stack.pop()
                if '[' in l:
                    stack.append('[')
                else:
                    stack.pop()
                
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"
    """Validate a single input line for correct nesting"""
    


def main(args):
    with open('output.txt', 'r') as file:
        for line in file:
            data = file.readlines(line)
        return data
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file


if __name__ == '__main__':
    main(sys.argv[1:])
