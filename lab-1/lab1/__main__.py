# Adapted from example lab

# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab1'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

from pathlib import Path
import argparse

from lab1.lab1 import process_files

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

in_path = Path(args.in_file)
out_path = Path(args.out_file)

# Here's the real entrypoint into the whole program. Reads the input file,
# performs the conversions, and then writes errors to stderr and the
# successful results to the output file. The input and output files are
# read from the command line input above.
with in_path.open('r') as input_file, out_path.open('w') as output_file:
    process_files(input_file, output_file)
