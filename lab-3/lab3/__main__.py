# Adapted from example lab

# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab3'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

from lab3.lab3 import process_files
from pathlib import Path
import argparse
import logging

try:
    arg_parser = argparse.ArgumentParser(exit_on_error=False)
    arg_parser.description = f"Use Huffman Encoding to compress and decompress data"
    arg_parser.add_argument("--frequency_table_file", type=str,
                            help="Pathname for the file containing the mapping from characters to frequencies")
    arg_parser.add_argument("--plaintext_file", type=str,
                            help="Pathname for the plain text that is to be compressed")
    arg_parser.add_argument("--compression_results_file", type=str,
                            help="Pathname for the filename for the ciphertext resulting from compression")
    arg_parser.add_argument("--compressed_file", type=str,
                            help="Pathname for input ciphertext that is to be decompressed")
    arg_parser.add_argument("--decompression_results_file", type=str,
                            help="Pathname for the filename for the plaintext resulting from decompression")
    arg_parser.add_argument("-l", "--level", type=str, default="INFO",
                            choices=["INFO", "WARNING", "ERROR",
                                     "DEBUG", "CRITICAL", "FATAL"],
                            help="Sets the level of the logger. Default INFO",
                            required=False)
    arg_parser.add_argument("-f", "--logfile", type=str, default="lab3.log",
                            help="Sets the filename where logs are written",
                            required=False)
    args = arg_parser.parse_args()

    frequency_table_file_path = Path(args.frequency_table_file)
    plaintext_file_path = Path(args.plaintext_file)
    compression_results_file_path = Path(args.compression_results_file)
    compressed_file_path = Path(args.compressed_file)
    decompression_results_file_path = Path(args.decompression_results_file)

    level = args.level
    logfilename = args.logfile

    logging.basicConfig(filename=logfilename,
                        level=args.level,
                        format="%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] - %(levelname)s - %(message)s",
                        datefmt="%Y-%m-%dT%H:%M:%S%z")

    logger = logging.getLogger(__name__)

    # Here's the real entrypoint into the whole program. Reads the input file,
    # performs the conversions, and then writes errors to stderr and the
    # successful results to the output file. The input and output files are
    # read from the command line input above.

    with frequency_table_file_path.open('r') as frequency_table_file, \
            plaintext_file_path.open('r') as plaintext_file, \
            compression_results_file_path.open('w') as compression_results_file, \
            compressed_file_path.open('r') as compressed_file, \
            decompression_results_file_path.open('w') as decompression_results_file:
        logger.info(
            f"compressing {plaintext_file_path} based on frequency table at {frequency_table_file_path} and writing to {compression_results_file_path}")
        logger.info(
            f"decompressing {compressed_file_path} based on frequency table at {frequency_table_file_path} and writing to {decompression_results_file_path}")

        process_files(
            frequency_table_file=frequency_table_file,
            plaintext_file=plaintext_file,
            compression_results_file=compression_results_file,
            compressed_file=compressed_file,
            decompression_results_file=decompression_results_file)

except Exception as e:
    arg_parser.print_help()
