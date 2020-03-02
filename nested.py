#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Janelle Kuhns and google on github"

import sys

openers = ['[', '(', '{', '<', '(*']
closers = [']', ')', '}', '>', '*)']

def is_nested(line):
    stack = []
    unbalanced = False
    pos = 0

    while line:
        token = line[0]
        if line[:2] == '(*' or line[:2] == '*)':
            token = line[:2]
        pos += 1
        if token in closers:
            index = closers.index(token)
            match = openers[index]
            if stack.pop() != match:
                unbalanced  = True
                break
        if token in openers:
            stack.append(token)

        line = line[len(token):]
    if stack or unbalanced:
        return 'No ' + str(pos)
    return 'Yes'
    


def main(args):
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as out:
            for line in f:
                read_output = is_nested(line)
                print(read_output)
                out.write(read_output + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
