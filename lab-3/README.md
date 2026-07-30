# Lab 3

## Prompt - Recursion - Converting Prefix to Postfix Expressions

This lab illustrates the use of a Huffman Encoding tree to compress and decompress strings. This has applications in encryption, and it is a useful illustration of trees and heaps. A Huffman Encoding Tree generates an encoding of a string by creating a tree structured according to the frequency of the character in a pre-specified source text for the frequency data. The goal is to have frequently occurring characters encoded with few characters, while less frequently occurring characters are allowed to consume more characters in the encoding.

The strings to encode and decode will be read in from files and output to files that are specified through command-line arguments. Along with these, a path to a frequency table for the characters used in the encoding will be provided through the command line. Errors will be printed to stderr for review. The lab is meant to be run as a module. See [Running Lab 3](#running-lab-3) below. The lab was written using the IDE VSCode. See [github.com/jllovet/jhu-en-605-202-su26-data-structures](https://github.com/jllovet/jhu-en-605-202-su26-data-structures) for additional setup details if required.


# Running Lab 2

```commandline
python -m lab3                           
usage: python3.14 -m lab3 [-h] [--frequency_table_file FREQUENCY_TABLE_FILE] [--plaintext_file PLAINTEXT_FILE]
                          [--compression_results_file COMPRESSION_RESULTS_FILE] [--compressed_file COMPRESSED_FILE]
                          [--decompression_results_file DECOMPRESSION_RESULTS_FILE] [-l {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}]
                          [-f LOGFILE]

Use Huffman Encoding to compress and decompress data

options:
  -h, --help            show this help message and exit
  --frequency_table_file FREQUENCY_TABLE_FILE
                        Pathname for the file containing the mapping from characters to frequencies
  --plaintext_file PLAINTEXT_FILE
                        Pathname for the plain text that is to be compressed
  --compression_results_file COMPRESSION_RESULTS_FILE
                        Pathname for the filename for the ciphertext resulting from compression
  --compressed_file COMPRESSED_FILE
                        Pathname for input ciphertext that is to be decompressed
  --decompression_results_file DECOMPRESSION_RESULTS_FILE
                        Pathname for the filename for the plaintext resulting from decompression
  -l, --level {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}
                        Sets the level of the logger. Default INFO
  -f, --logfile LOGFILE
                        Sets the filename where logs are written
```

For example, presume you have the following folder structure (ignoring the contents of lab2 for the moment).

```
.
├── lab3
│   ├── ...
└── resources
    ├── input
    │   ├── ClearText.txt 
    │   ├── Encoded.txt
    │   └── FreqTable.txt
    └── output
        ├── DecodingResults.txt 
        └── EncodingResults.txt
```

You can run the program from the command line like this:

```shell
python -m lab3 \
    --level DEBUG \
    --logfile demo.lab3.log \
    --frequency_table_file ./resources/input/FreqTable.txt \
    --plaintext_file ./resources/input/ClearText.txt \
    --compression_results_file ./resources/output/EncodingResults.txt \
    --compressed_file ./resources/input/Encoded.txt \
    --decompression_results_file ./resources/output/DecodingResults.txt
```

If there are errors, they will be printed to stderr, which means that they will appear on your terminal, but they are informational. Along with those errors, you will be given some information that might help with navigating the errors. You will have to redirect stderr if you want to collect it somewhere. The output of the program will be written to `resources/output/EncodingResults.txt` and to `resources/output/DecodingResults.txt`.

`resources/input/in.txt` might contain the following items:

```txt
Sally sells seashells by the seashore.
Peter Piper picked a peck of pickled peppers a peck of pickled peppers Peter Piper picked.
Houston, the Eagle has landed.
Is that your final answer?
```

Running the program will produce the following output in `resources/output/EncodingResults.txt`:

```txt
11101111100010001101101111001000010001111011100101111111101101101000010001111011000101101100111011010111001011111111011011111101000010
10100010100101010001010011001101000101000101001100111010001000100110011111101000101101000100111100110110100110011101000100000101001100101000101010010100010100011101111110100010110100010011110011011010011001110100010000010100110010100010101001010001010001110101000101001010100010100110011010001010001010011001110100010001001100
11011111101011111101001111100111100111011010010111111010100010101101111111111000011111101110110001001100
1100111101001110111111110011011011111010111100001101110010111111110001111110111111000110101000
```

Along with this, the program will print the following to stderr:

```text

********************************************************************************

STAGE 1: COMPRESSION

********************************************************************************

Sally sells seashells by the seashore.
Peter Piper picked a peck of pickled peppers a peck of pickled peppers Peter Piper picked.
Houston, the Eagle has landed.
Is that your final answer?

********************************************************************************

STAGE 2: DECOMPRESSION

********************************************************************************

01011001010110011111011011
10110000101010011011101101100010110010101100010111000110111
11111110001000111111101011111011001111111000100011111000001010000001110010111

********************************************************************************

The tree in preorder is: [MLKJVWEDFNRTPGZQXYUBICHSOA 413], [MLKJVWEDFN 169], [MLKJVW 80], [ML 39], [M 19], [L 20], [KJVW 41], [KJV 20], [K 10], [JV 10], [J 5], [V 5], [W 21], [EDFN 89], [E 42], [DFN 47], [DF 23], [D 11], [F 12], [N 24], [RTPGZQXYUBICHSOA 244], [RTPGZQXYU 106], [RT 50], [R 25], [T 25], [PGZQXYU 56], [PG 27], [P 13], [G 14], [ZQXYU 29], [ZQXY 14], [ZQX 6], [Z 3], [QX 3], [Q 1], [X 2], [Y 8], [U 15], [BICHSOA 138], [BICH 66], [BI 32], [B 16], [I 16], [CH 34], [C 17], [H 17], [SOA 72], [S 35], [OA 37], [O 18], [A 19]

********************************************************************************

The code is: A: 11111; B: 11000; C: 11010; D: 01100; E: 010; F: 01101; G: 10101; H: 11011; I: 11001; J: 001010; K: 00100; L: 0001; M: 0000; N: 0111; O: 11110; P: 10100; Q: 10110010; R: 1000; S: 1110; T: 1001; U: 10111; V: 001011; W: 0011; X: 10110011; Y: 101101; Z: 1011000
```

Where possible, error messages will point to specific structural problems for each case.

# Enhancements!

Below is a discussion of some of the enhancements implemented here above the requirements of the lab.

## Running Tests

This lab uses `unittest`, a package available in the python standard library, to ensure that the behavior of the code can remain consistent even as changes are made to the codebase.

Clone the repo from Github at [github.com/jllovet/jhu-en-605-202-su26-data-structures](https://github.com/jllovet/jhu-en-605-202-su26-data-structures).

```shell
git clone https://github.com/jllovet/jhu-en-605-202-su26-data-structures.git
```

Then you can run the full test suite like follows.

```shell
cd jhu-en-605-202-su26-data-structures/lab-3
python -m unittest discover -s lab3/tests
```

## Logging

This lab uses the python logging package to write logs. Most of these are configured to only be emitted when the logger leve is set to debug, but there are a number of logs that are produced at an info, error, and debug level. The log level can be set by the user through the command line. By default this is INFO. Recall the usage:

```commandline
python -m lab3                           
usage: python3.14 -m lab3 [-h] [--frequency_table_file FREQUENCY_TABLE_FILE] [--plaintext_file PLAINTEXT_FILE]
                          [--compression_results_file COMPRESSION_RESULTS_FILE] [--compressed_file COMPRESSED_FILE]
                          [--decompression_results_file DECOMPRESSION_RESULTS_FILE] [-l {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}]
                          [-f LOGFILE]

Use Huffman Encoding to compress and decompress data

options:
  -h, --help            show this help message and exit
  --frequency_table_file FREQUENCY_TABLE_FILE
                        Pathname for the file containing the mapping from characters to frequencies
  --plaintext_file PLAINTEXT_FILE
                        Pathname for the plain text that is to be compressed
  --compression_results_file COMPRESSION_RESULTS_FILE
                        Pathname for the filename for the ciphertext resulting from compression
  --compressed_file COMPRESSED_FILE
                        Pathname for input ciphertext that is to be decompressed
  --decompression_results_file DECOMPRESSION_RESULTS_FILE
                        Pathname for the filename for the plaintext resulting from decompression
  -l, --level {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}
                        Sets the level of the logger. Default INFO
  -f, --logfile LOGFILE
                        Sets the filename where logs are written
```

To set the log level to DEBUG and set the location of the logfile, for example, the user could run a command like the following:

```commandline
python -m lab3 \
    --level DEBUG \
    --logfile demo.lab3.log \
    --frequency_table_file ./resources/input/FreqTable.txt \
    --plaintext_file ./resources/input/ClearText.txt \
    --compression_results_file ./resources/output/EncodingResults.txt \
    --compressed_file ./resources/input/Encoded.txt \
    --decompression_results_file ./resources/output/DecodingResults.txt
```

This will produce a logfile called `demo.lab3.log` at `DEBUG` level with messages similar to the following:

```log
2026-07-30T01:15:07-0400 - [__main__.py:<module>:62] - INFO - compressing resources/input/ClearText.txt based on frequency table at resources/input/FreqTable.txt and writing to resources/output/EncodingResults.txt
2026-07-30T01:15:07-0400 - [__main__.py:<module>:64] - INFO - decompressing resources/input/Encoded.txt based on frequency table at resources/input/FreqTable.txt and writing to resources/output/DecodingResults.txt
...
2026-07-30T01:15:07-0400 - [encode.py:build_huffman_encoding_tree:168] - DEBUG - Building Huffman Encoding Tree
2026-07-30T01:15:07-0400 - [encode.py:frequency_to_encoding_data:118] - DEBUG - Converting frequency table to encoding data
2026-07-30T01:15:07-0400 - [encode.py:frequency_to_encoding_data:119] - DEBUG - freq_table: ['A - 19', 'B - 16', 'C - 17', 'D - 11', 'E - 42', 'F - 12', 'G - 14', 'H - 17', 'mmmmmmmmmmm', 'I - 16', 'J - 5', 'K - 10', 'L - 20', 'M - 19', 'N - 24', 'O - 18', 'P - 13', 'Q - 1', 'R - 25', 'S - 35', 'T - 25', 'U - 15', 'V - 5', 'W - 21', 'X - 2', 'Y - 8', 'Z - 3']
...
2026-07-30T01:15:07-0400 - [encode.py:frequency_to_encoding_data:128] - ERROR - The frequency table is invalid in row 8: 'mmmmmmmmmmm' should be in the form 'A - 1'
2026-07-30T01:15:07-0400 - [lab3.py:process_files:82] - WARNING - Errors raised 15
```

Inspection of the log file produced reveals that the log messages have a timestamp, the file, function, and line number where the log was produced, along with the severity of the message.


## Generator to Traverse Tree in Post-Order

As in my previous lab, I experimented in this lab with using python generators after a conversation with the professor in office hours. Using `yield` in the `__iter__` function of the `Node` class in the correct order, I was able to make extracting the postfix expression from the tree simple. I form an abstract syntax tree, and then I use the `__iter__` function to iterate over the nodes in post-order, meaning that I start with the leaves, reading the left child, then the right child, then the parent, left to right, up the tree recursively. What's more, in this lab, I implemented additional methods such as `preorder`, `postorder`, and `inorder` with attending functions for forcing the evaluation of the tree traversals and outputting the results as a str. I made use of this in the functions that print the encoding for the user.

I'm especially indebted to the strategy described here: https://martinheinz.dev/blog/88.

Consider these methods on the `Node` class.

```python
def preorder_as_str(self):
    """Forces evaluation of preorder iteration and joins elements into string"""
    return ", ".join([str(s) for s in self.preorder()])

def preorder(self):
    """Yield the nodes of the tree in preorder

    Inspired by the strategy described here: https://martinheinz.dev/blog/88

    Given the tree: ABCDEFG

    preorder yields the tree's elements as ABDECFG

    Args:
        None

    Returns:
        Yields the elements of the tree in preorder.

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        False
    """
    yield self.data
    if self.left:
        yield from self.left.__iter__(order="preorder")
    if self.right:
        yield from self.right.__iter__(order="preorder")
```

## Custom Comparison Operators

I used a `MinHeap` to build a priority queue to use in the building of the Huffman Encoding Tree. While doing so I found myself constrained by my previous decision to create an `EncodingData` type. How could I do the comparisons in the `MinHeap` between nodes if I needed to compare the `EncodingData`? I solved this by writing comparison operators in dunder methods in the `EncodingData` class. By defining the methods directly into the class, I was able to provide comparisons with tie breakers, per our requirements. Importantly, these comparison methods allow the objects of this type to be compared with the built-in comparison operators like `<`, which made the implementation of the priority queue with a `MaxHeap` much easier.

Consider this example operator from the `EncodingData` class.

```python
def __lt__(self, other):
    # Sorting: score has highest priority, then length, then alphabetic order
    # Score
    if self.score < other.score:
        return True
    if self.score > other.score:
        return False
    # implies that self.score == other.score
    # Length
    if len(self.characters) < len(other.characters):
        return True
    if len(self.characters) > len(other.characters):
        return False
    # implies len(self.characters) == len(other.characters)
    # Alphabetic order
    return self.characters < other.characters
```