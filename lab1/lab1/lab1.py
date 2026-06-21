from sys import stderr
from typing import TextIO
import logging
import lab1.converter.converter as converter
import lab1.parse.prefix as prefix

logging.basicConfig(filename='lab1.log', level=logging.INFO)


def print_errors(errors):
    error_preamble = [
        f"""WARNING: {len(errors)} errors found during conversion
WARNING: Invalid expressions not written to output file\n
Check expressions to ensure the are well formed and only use allowed symbols.\n
Note: whitespace is not allowed. Expressions with whitespace will be rejected.\n
Allowed symbols: ABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/$()\n
Example valid expressions:
\t(base case):\t'A'\t-> '{converter.pre2post('A')}'
\t(single op):\t'+AB'\t-> '{converter.pre2post('+AB')}'
\t(more ops):\t'-+ABC'\t-> '{converter.pre2post('-+ABC')}'""",
        f"-"*80,
        "ERRORS:"
    ]
    for msg in error_preamble:
        print(msg, file=stderr)

    for error in errors:
        print(error, file=stderr)


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads prefix expressions from an input file, converts them into
    postfix expressions directly, and writes them to an output file.
    Prints usage info and error info to stderr if there are errors.
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    """
    logging.info("called process_files")
    lines = input_file.read().splitlines()
    errors = []
    for line_number, line in enumerate(lines):
        if line is not None and line != "":
            try:
                postfix = converter.pre2post(line)
            except ValueError as e:
                errors.append(
                    f"{input_file.name} - line {line_number + 1}: {e}")
                continue
            output_file.write(postfix)
            output_file.write("\n")
    if errors:
        print_errors(errors)
