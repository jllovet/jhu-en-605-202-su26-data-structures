from sys import stderr
from typing import TextIO, List
import lab3.huffman.encode as e
import lab3.huffman.decode as d
import logging
logger = logging.getLogger(__name__)


def separator():
    """Prints a boundary to separate console output visually"""
    print("\n" + "*"*80 + "\n", file=stderr)


def msg(s, before=False, after=True):
    """Prints a line to stderr with an optional separator before and after"""
    if before:
        separator()
    print(s, file=stderr)
    if after:
        separator()


def echo(lines: List):
    """Prints each line of the provided list to stderr"""
    for l in lines:
        print(l.strip(), file=stderr)


def process_files(frequency_table_file: TextIO,
                  plaintext_file: TextIO,
                  compression_results_file: TextIO,
                  compressed_file: TextIO,
                  decompression_results_file: TextIO) -> None:
    """Reads -> converts -> writes compression and decompression

    Reads frequency table, data to compress, and data to decompress from
    input files, and writes them to an output file.
    This is the logical entrypoint to the program when called as a module,
    where __main__ will call it with files passed from the command line.

    Args:
    frequency_table_file: TextIO is an opened text file set to read mode
    This is the file containing the mapping from characters to frequencies

    plaintext_file: TextIO is an opened text file set to read mode
    This contains the plain text that is to be compressed

    compression_results_file: TextIO is an opened text file set to write mode
    This contains the ciphertext as a result of compression

    compressed_file: TextIO is an opened text file set to read mode
    This contains input ciphertext that is to be decompressed

    decompression_results_file: TextIO is an opened text file set to write mode
    This contains the plaintext decoded data as a result of decompression

    Returns:
        None

    Raises:
        None

    Side Effects:
        Reads from frequency_table_file
        Reads from plaintext_file
        Reads from compressed_file
        Writes to compression_results_file
        Writes to decompression_results_file
        Prints errors to stderr
        Writes to logs

    Idempotent:
        True
    """

    raised_errors = []
    frequency_table_lines = frequency_table_file.read().splitlines()
    encoding_tree = e.build_huffman_encoding_tree(
        freq_table=frequency_table_lines)
    codes = e.get_huffman_codes_from_tree(encoding_tree)

    msg(f"STAGE 1: COMPRESSION", before=True, after=True)
    logger.info("Reading lines from plaintext input file")
    plaintext_lines = plaintext_file.readlines()
    echo(plaintext_lines)

    compression_results = []
    for index, s in enumerate(plaintext_lines):
        try:
            res = e.compress(s, encoding_tree)
            compression_results.append(res)
            logger.debug(f"Compressed {s}")
        except ValueError as err:
            logger.error(f"Error in line {index+1} of plaintext input. Could not compress {s}: {err}")
            raised_errors.append(
                f"Error in line {index+1} of plaintext input. Could not compress {s}")
    for line in compression_results:
        compression_results_file.write(line)
        compression_results_file.write("\n")

    # DECOMPRESSION
    msg(f"STAGE 2: DECOMPRESSION", before=True, after=True)
    compressed_lines = compressed_file.readlines()
    echo(compressed_lines)

    decompression_results = []
    for index, s in enumerate(compressed_lines):
        try:
            res = d.decompress(s, encoding_tree)
            decompression_results.append(res)
        except ValueError as err:
            logger.error(f"ERROR: line {index+1} of compressed input. Could not decompress {s}: {err}")
            raised_errors.append(
                f"ERROR: line {index+1} of compressed input. Could not decompress {s}")
    for line in decompression_results:
        decompression_results_file.write(line)
        decompression_results_file.write("\n")

    msg(f"The tree in preorder is: {encoding_tree.preorder_as_str()}",
        before=True, after=True)
    msg(
        f"The code is: {'; '.join([f'{k}: {v}' for k, v in sorted(codes.items())])}", after=False)
    if raised_errors:
        logger.warning("Errors raised")
        print_errors(raised_errors)


def print_errors(errors: list[str]) -> None:
    """Prints error information to stderr
    Args:
        errors: list[str] where each element contains details
        of the error that occurred, e.g. line number, message

    Returns:
        None

    Raises:
        None

    Side Effects:
        Prints to stderr

    Idempotent:
        True
    """
    error_preamble = [
        f"""\nWARNING: {len(errors)} errors found during run!""",
        "-"*80
    ]
    for s in error_preamble:
        print(s, file=stderr)

    for error in errors:
        print(error, file=stderr)
