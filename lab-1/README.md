# Lab 1

## Prompt - Use of Stacks - Converting Prefix to Postfix Expressions

This lab illustrates the use of stacks in the conversion of prefix expressions to postfix expressions. The prefix expressions will be read in from a file and then output to a file, both of which are provided at the command line. Errors will be printed to stderr for review. The lab is meant to be run as a module. See [Running Lab 1](#running-lab-1) below.

What is the lab doing again? We want to convert expressions in this form: `+AB` to this form `AB+`. Both of these are equivalent to the probably more familiar infix notation for the same expression `A+B`. We want to convert from Polish notation to Reverse Polish notation.

# Running Lab 1

```commandline
usage: python -m lab1 [-h] in_file out_file

Convert prefix -> postfix expressions from in_file and write them to out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

options:
  -h, --help  show this help message and exit
```

For example, presume you have the following folder structure (ignoring the contents of lab1 for the moment).

```
.
├── lab1
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
python -m lab1 resources/input/in.txt resources/output/output.txt
```

If there are errors, they will be printed to stderr, which means that they will appear on your terminal, but they are informational. You will have to redirect stderr if you want to collect it somewhere. The output of the program will be written to `output.txt`.

`resources/input/in.txt` might contain the following items:

```txt
A
AB
AB+
+AA
```

Running the program will produce the following output in `resources/output/output.txt`:

```txt
A
AA+
```

And it will also print the following error:

```stderr
WARNING: 2 errors found during conversion
WARNING: Invalid expressions not written to output file

Check expressions to ensure the are well formed and only use allowed symbols.

Note: whitespace is not allowed. Expressions with whitespace will be rejected.

Allowed symbols: ABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/$()

Example valid expressions:
        (base case):    'A'     -> 'A'
        (single op):    '+AB'   -> 'AB+'
        (more ops):     '-+ABC' -> 'AB+C-'
--------------------------------------------------------------------------------
ERRORS:
resources/input/in.txt - line 2: 'AB' is not a valid prefix expression
resources/input/in.txt - line 3: 'AB+' is not a valid prefix expression
```

## Running Tests

This lab uses `unittest`, a package available in the python standard library, to ensure that the behavior of the code can remain consistent even as changes are made to the codebase.

Clone the repo from Github at [github.com/jllovet/jhu-en-605-202-su26-data-structures](https://github.com/jllovet/jhu-en-605-202-su26-data-structures).

```shell
git clone https://github.com/jllovet/jhu-en-605-202-su26-data-structures.git
```

Then you can run the full test suite like follows.

```shell
cd jhu-en-605-202-su26-data-structures/lab-1
python -m unittest discover -s lab1/tests
```