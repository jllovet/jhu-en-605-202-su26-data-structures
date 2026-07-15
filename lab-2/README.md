# Lab 2

## Prompt - Use of Recursion - Converting Prefix to Postfix Expressions

This lab illustrates the use of recursion in the conversion of prefix expressions to postfix expressions. The prefix expressions will be read in from a file and then output to a file, both of which are provided at the command line. Errors will be printed to stderr for review. The lab is meant to be run as a module. See [Running Lab 2](#running-lab-2) below. The lab was written using the IDE VSCode. See [github.com/jllovet/jhu-en-605-202-su26-data-structures](https://github.com/jllovet/jhu-en-605-202-su26-data-structures) for additional setup details if required.

What is the lab doing again? We want to convert expressions in this form: `+AB` to this form `AB+`. Both of these are equivalent to the probably more familiar infix notation for the same expression `A+B`. We want to convert from Polish notation to Reverse Polish notation.

# Running Lab 2

```commandline
usage: python3 -m lab2 [-h] [-l {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}]
                          [-f LOGFILE]
                          in_file out_file

Convert prefix -> postfix expressions from in_file and write them to out_file

positional arguments:
  in_file               Input File Pathname
  out_file              Output File Pathname

options:
  -h, --help            show this help message and exit
  -l, --level {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}
                        Sets the level of the logger. Default INFO
  -f, --logfile LOGFILE
                        Sets the filename where logs are written
```

For example, presume you have the following folder structure (ignoring the contents of lab2 for the moment).

```
.
├── lab2
│   ├── ...
└── resources
    ├── input
    │   ├── good.txt
    │   └── in.txt
    └── output
        └── output.txt
```

You can run the program from the command line like this:

```shell
python -m lab2 resources/input/in.txt resources/output/output.txt
```

If there are errors, they will be printed to stderr, which means that they will appear on your terminal, but they are informational. Along with those errors, you will be given some information that might help with navigating the errors. You will have to redirect stderr if you want to collect it somewhere. The output of the program will be written to `resources/output/output.txt`.

`resources/input/in.txt` might contain the following items:

```txt
A
AB
AB+
+AA
```

Running the program will produce the following output in `resources/output/output.txt`:

```txt
Processing expressions below:
A
AB
AB+
+AA

WARNING: 2 errors found during conversion!
Check expressions are well-formed prefix expressions and only use allowed symbols.

Allowed symbols are alphabetical characters and any of: +-*/$()

Example valid expressions:
        (base case):    'A'     -> 'A'
        (single op):    '+AB'   -> 'AB+'
        (more ops):     '-+ABC' -> 'AB+C-'
--------------------------------------------------------------------------------
ERROR: resources/input/readme.txt - line 2: 'AB' could not be processed. Prefix expressions can't start with an operand.
ERROR: resources/input/readme.txt - line 3: 'AB+' could not be processed. Prefix expressions can't start with an operand.
```

Where possible, the error messages will point to specific structural problems for each case.

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
cd jhu-en-605-202-su26-data-structures/lab-2
python -m unittest discover -s lab2/tests
```

### cleaner.clean

The conversion in `lab2/convert/converter.py` uses a recursive implementation to perform the conversion of prefix to postfix expressions. There is a testing utility in this version of the lab that iteratively strips whitespace and other irrelevant characters from the input expressions. That is used in the unit tests to ensure that whatever changes are made to the recursive implementation, they will continue to produce equivalent results whether or not the input expressions have spaces and other irrelevant characters.

See the following test for example:

```python
def test_converter_pre2post_converts_expressions_identically_with_and_without_whitespace(self):
        expression = "-+A BC      "
        clean_expression = cleaner.clean(expression)
        self.assertEqual(
            converter.pre2post(expression),
            converter.pre2post(clean_expression)
        )
```

### Unicode support

In this version of the lab, the operand support is much more flexible. In lab1, the only operands that were supported were uppercase ascii characters. Now, alphabetic operands are supported from other alphabets. This is validated continuously through unit tests. See the example below that shows that the converter succeeds even when mixing multiple alphabets, even if they are written in different directions. (The example uses polytonic Ancient Greek, Russian, and Hebrew letters.)

```
class TestSymbolClassifiers(unittest.TestCase):
...
    def test_is_allowed(self):
        self.assertTrue(validate.is_allowed("A"))
        self.assertTrue(validate.is_allowed("B"))
...
        self.assertTrue(validate.is_allowed("a"))
        self.assertTrue(validate.is_allowed("ф"))  # Unicode: Cyrillic
        # Unicode: Polytonic Ancient Greek
        self.assertTrue(validate.is_allowed("ἄ"))
```

```
class TestPre2Post(unittest.TestCase):
...
def test_converter_pre2post_converts_expressions_with_multiple_alphabets(self):
        expression = "$ἄ +фכ"
        expected = "ἄфכ+$"
        self.assertEqual(
            converter.pre2post(expression),
            expected
        )
```

## Logging

This version of the lab uses the python logging package to write logs. Most of these are configured to only be emitted when the logger leve is set to debug, but there are a number of logs that are produced at an info and error level. The log level can be set by the user through the command line. By default this is Recall the usage:

```commandline
usage: python3 -m lab2 [-h] [-l {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}]
                          [-f LOGFILE]
                          in_file out_file

Convert prefix -> postfix expressions from in_file and write them to out_file

positional arguments:
  in_file               Input File Pathname
  out_file              Output File Pathname

options:
  -h, --help            show this help message and exit
  -l, --level {INFO,WARNING,ERROR,DEBUG,CRITICAL,FATAL}
                        Sets the level of the logger. Default INFO
  -f, --logfile LOGFILE
                        Sets the filename where logs are written
```

To set the log level to DEBUG, for example, the user could run a command like the following:

```commandline
python -m lab2 resources/input/readme.txt resources/output/output.txt --level DEBUG
```

Similarly, the user can set the name of the logfile. 

```commandline
python -m lab2 resources/input/readme.txt resources/output/output.txt --level DEBUG --logfile mylab2.log
```

This will produce a logfile called `mylab2.log` with the contents below:

```log
2026-07-15T01:21:01-0400 - [__main__.py:<module>:46] - INFO - processing input file resources/input/readme.txt and writing to resources/output/output.txt
2026-07-15T01:21:01-0400 - [lab2.py:process_files:41] - INFO - Beginning to process expressions
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:152] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:pre2post:314] - DEBUG - POSTFIX EXPRESSION: 'A'
2026-07-15T01:21:01-0400 - [lab2.py:process_files:46] - DEBUG - Converted 'A' -> 'A'
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: 'AB'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:120] - ERROR - 'AB' could not be processed. Prefix expressions can't start with an operand.
2026-07-15T01:21:01-0400 - [converter.py:pre2post:317] - ERROR - Reraising error: 'AB' could not be processed. Prefix expressions can't start with an operand.
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: 'AB+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:120] - ERROR - 'AB+' could not be processed. Prefix expressions can't start with an operand.
2026-07-15T01:21:01-0400 - [converter.py:pre2post:317] - ERROR - Reraising error: 'AB+' could not be processed. Prefix expressions can't start with an operand.
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: '+AA'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: '+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:167] - DEBUG - FOUND OPERATOR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:A
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:152] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:214] - DEBUG - AT DEPTH 0: OPERATORS:1 OPERANDS:2
2026-07-15T01:21:01-0400 - [converter.py:pre2post:314] - DEBUG - POSTFIX EXPRESSION: 'AA+'
2026-07-15T01:21:01-0400 - [lab2.py:process_files:46] - DEBUG - Converted '+AA' -> 'AA+'
2026-07-15T01:21:01-0400 - [lab2.py:process_files:65] - WARNING - Errors raised
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:152] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:pre2post:314] - DEBUG - POSTFIX EXPRESSION: 'A'
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: '+AB'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: '+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:167] - DEBUG - FOUND OPERATOR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:A
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'B'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:152] - DEBUG - MAKING NODE FROM:'B'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:214] - DEBUG - AT DEPTH 0: OPERATORS:1 OPERANDS:2
2026-07-15T01:21:01-0400 - [converter.py:pre2post:314] - DEBUG - POSTFIX EXPRESSION: 'AB+'
2026-07-15T01:21:01-0400 - [converter.py:pre2post:307] - INFO - Attempting to convert: '-+ABC'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: '-'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:-
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'-'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:167] - DEBUG - FOUND OPERATOR:-
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: '+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'+'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:167] - DEBUG - FOUND OPERATOR:+
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:A
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'A'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'B'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:161] - DEBUG - CURRENT CHAR:B
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:162] - DEBUG - MAKING NODE FROM:'B'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:134] - DEBUG - Considering whether to skip characters
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:135] - DEBUG - CURRENT: 'C'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:152] - DEBUG - MAKING NODE FROM:'C'
2026-07-15T01:21:01-0400 - [converter.py:_pre2post:214] - DEBUG - AT DEPTH 0: OPERATORS:2 OPERANDS:3
2026-07-15T01:21:01-0400 - [converter.py:pre2post:314] - DEBUG - POSTFIX EXPRESSION: 'AB+C-'
2026-07-15T01:21:01-0400 - [lab2.py:print_errors:105] - ERROR - ERROR: resources/input/readme.txt - line 2: 'AB' could not be processed. Prefix expressions can't start with an operand.
2026-07-15T01:21:01-0400 - [lab2.py:print_errors:105] - ERROR - ERROR: resources/input/readme.txt - line 3: 'AB+' could not be processed. Prefix expressions can't start with an operand.
```

Inspection of the log file produced reveals that the log messages have a timestamp, the file, function, and line number where the log was produced, along with the severity of the message. (Note that the repetition of "ERROR" is because the second instance is shown to the user. It's part of the actual error message in this case.)


## Generator to Traverse Tree in Post-Order

Based on a conversation with the professor during office hours, I experimented in this lab with using python's generators. Using `yield` in the `__iter__` function of the `Node` class in the correct order, I was able to make extracting the postfix expression from the tree simple. I form an abstract syntax tree, and then I use the `__iter__` function to iterate over the nodes in post-order, meaning that I start with the leaves, reading the left child, then the right child, then the parent, left to right, up the tree recursively. In the future I will experiment more with using generators and iterators to have lazy evaluation in python.

While I read and watched multiple resources to learn about generators, I'm especially indebted to the strategy described here: https://martinheinz.dev/blog/88.

Here is `Node.__iter__`:

```python
def __iter__(self):
    """Yield the nodes of the tree in post-order

    Inspired by the strategy described here: https://martinheinz.dev/blog/88
    
    Args:
        None

    Returns:
        Yields the elements of the tree in post-order.

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        False
    """
    if self.left:
        yield from self.left
    if self.right:
        yield from self.right
    yield self.data
```

## Custom Error Types

In addition to the items above, I inlcuded custom error types in this lab, to experiment with the inheritance and the pattern of specific sentinel error types. They allow for more precise error types in the function `_pre2post` than `ValueError`, for example. The illustration below shows how I defined a base custom error class: `InvalidExpressionError`, which itself inherits from `ValueError`. From there there are three child error types inheriting from it, each with its own default error message.

```python
class InvalidExpressionError(ValueError):
    def __init__(self, msg: str):
        super().__init__(msg)


class TooManyOperatorsError(InvalidExpressionError):
    def __init__(self, msg: str = "Too many operators provided in expression"):
        super().__init__(msg)


class TooManyOperandsError(InvalidExpressionError):
    def __init__(self, msg: str = "Too many operands provided in expression"):
        super().__init__(msg)


class IllegalOperandError(InvalidExpressionError):
    def __init__(self, msg: str = "Illegal operand provided in expression"):
        super().__init__(msg)
```
