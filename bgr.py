#!/usr/bin/env python3

import random

# simple implementation of BGR
OPS = [
    lambda a, b: a and b, # and
    lambda a, b: a or b, # or
    lambda a, b: not (a and b), # nand
    lambda a, b: a != b, # xor
    lambda a, b: not (a or b),
]


class BGR:
    def __init__(self, size):
        self.size = size
        self.nodes = [False] * size
        self.ops = random.choices(OPS, k = size)
        self.left = random.choices(range(size), k = size)
        self.right = random.choices(range(size), k = size)
        self.lock = [False] * size

    def iter(self):
        
        self.nodes = [
            self.ops[i](self.nodes[self.left[i]],
                        self.nodes[self.right[i]]) if not self.lock[i] else self.nodes[i]
            for i in range(self.size)]

test = BGR(10)
print(test.nodes)
test.iter()
print(test.nodes)
