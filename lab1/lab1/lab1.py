from sys import stderr
from typing import TextIO
import logging
import lab1.converter.converter as converter
import lab1.parse.prefix as prefix

logging.basicConfig(filename='lab1.log', level=logging.INFO)


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads prefix expressions from an input file, converts them into
    postfix expressions directly, and writes them to an output file.
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    """
    logging.info("called process_files")
    lines = input_file.read().splitlines()
    errors = []
    for line in lines:
        if line is not None and line != "":
            try:
                postfix = converter.pre2post(line)
            except ValueError as e:
                errors.append(f"{e}")
                continue
            output_file.write(postfix)
            output_file.write("\n")
    if errors:
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
            f"-"*80
        ]
        for msg in error_preamble:
            print(msg, file=stderr)

        for error in errors:
            print(error, file=stderr)
