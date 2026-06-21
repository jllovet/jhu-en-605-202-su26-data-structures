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

    next_line = input_file.readline()
    while next_line is not None and next_line != "":
        try:
            expression = next_line
        except ValueError as e:
            print(e, file=stderr)
            continue
        finally:
            next_line = input_file.readline()

        postfix = converter.pre2post(expression)
        output_file.write(postfix)
        output_file.write("\n")
