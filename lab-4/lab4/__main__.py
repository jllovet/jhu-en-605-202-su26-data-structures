# Adapted from example lab

# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m lab2'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

from lab4.lab4 import process_files
from pathlib import Path
import argparse
import logging

try:
    arg_parser = argparse.ArgumentParser(exit_on_error=False)
    arg_parser.description = f"Run sorting experiments to generate performance metrics for different algorithms"
    arg_parser.add_argument("in_dir", type=str, help="Path to dir containing input files")
    arg_parser.add_argument("out_dir", type=str, help="Path to dir containing output files")
    arg_parser.add_argument("-l", "--level", type=str, default="INFO",
                            choices=["INFO", "WARNING", "ERROR",
                                     "DEBUG", "CRITICAL", "FATAL"],
                            help="Sets the level of the logger. Default INFO",
                            required=False)
    arg_parser.add_argument("-f", "--logfile", type=str, default="lab4.log",
                            help="Sets the filename where logs are written",
                            required=False)
    args = arg_parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)

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

    # TODO: Rewrite to handle all files and route performance metrics
    with in_dir.open('r') as input_file, out_dir.open('w') as output_file:
        logger.info(
            f"processing input file {in_dir} and writing to {out_dir}")
        process_files(input_file, output_file)

except Exception as e:
    arg_parser.print_help()
