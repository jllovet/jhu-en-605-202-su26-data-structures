from sys import stderr
from typing import TextIO
import logging

logging.basicConfig(filename='lab1.log', level=logging.INFO)

def convert_value(s: str):
    return s

def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads prefix expressions from an input file, converts them into
    postfix expressions directly, and writes them to an output file.
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    """
    logging.info("called process_files")
    print("test")
