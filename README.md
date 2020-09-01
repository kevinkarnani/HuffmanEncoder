# HuffmanEncoder

## Introduction

This is a modified and upgraded version of a Huffman encoder I wrote for my data structures class.

## Getting Started

### Prerequisites

You must have Python 3.x installed.

### Functionality

Given characters and frequencies, it prints the tree structure as well as the encoding of the characters.

For example, given this input:

```
Welcome to Huffman Encoder!
Add a Letter: a
Frequency of Letter: 7
Add another letter? (y/n)
y
Add a Letter: a
Frequency of Letter: 8
Letter 'a' already added.
Add a Letter: b
Frequency of Letter: 9
Add another letter? (y/n)
y
Add a Letter: c
Frequency of Letter: 12
Add another letter? (y/n)
y
Add a Letter: d
Frequency of Letter: 22
Add another letter? (y/n)
y
Add a Letter: e
Frequency of Letter: 23
Add another letter? (y/n)
y
Add a Letter: f
Frequency of Letter: 27
Add another letter? (y/n)
n
Okay, lets start!
```

The output will look like:

```
Parent: 6, Left: None, Right: None
Parent: 6, Left: None, Right: None
Parent: 7, Left: None, Right: None
Parent: 8, Left: None, Right: None
Parent: 8, Left: None, Right: None
Parent: 9, Left: None, Right: None
Parent: 7, Left: 0, Right: 1
Parent: 9, Left: 2, Right: 6
Parent: 10, Left: 3, Right: 4
Parent: 10, Left: 5, Right: 7
Parent: None, Left: 8, Right: 9
a : 1110
b : 1111
c : 110
d : 00
e : 01
f : 10
```

### Running The Encoder

After downloading the code, run:

```bash
./huffman.py
```

## Author

Kevin Karnani