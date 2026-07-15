# Adapted from example lab

# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab2'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

from lab2.lab2 import process_files
from pathlib import Path
import argparse
import logging

try:
    arg_parser = argparse.ArgumentParser(exit_on_error=False)
    arg_parser.description = f"Convert prefix -> postfix expressions from in_file and write them to out_file"
    arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
    arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
    arg_parser.add_argument("-l", "--level", type=str, default="INFO",
                            choices=["INFO", "WARNING", "ERROR",
                                     "DEBUG", "CRITICAL", "FATAL"],
                            help="Sets the level of the logger. Default INFO",
                            required=False)
    arg_parser.add_argument("-f", "--logfile", type=str, default="lab2.log",
                            help="Sets the filename where logs are written",
                            required=False)
    args = arg_parser.parse_args()

    in_path = Path(args.in_file)
    out_path = Path(args.out_file)

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
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        logger.info(
            f"processing input file {in_path} and writing to {out_path}")
        process_files(input_file, output_file)

except Exception as e:
    arg_parser.print_help()
