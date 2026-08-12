from sys import stderr
from typing import TextIO, IO, Any
import json

from lab4.sort.context import Algorithm
import lab4.sort.quick as quick
import logging
logger = logging.getLogger(__name__)


def process_files(input_file: TextIO, output_file: TextIO, stats_file: IO[Any], algorithm: Algorithm) -> None:
    """Reads -> sorts -> writes sorted files and a stats file

    Args:
        input_file: TextIO is an opened text file set to read mode, and it
        contains lists of numbers to sort
        output_file: TextIO is an opened text file set to write mode, and it
        is the file the sorted lists are written to
        stats_file: TextIO is an opened text file set to append mode, and it
        is the file where statistics about the sorting algorithms are written
        algorithm: The algorithm that is used for quicksort

    Returns:
        None

    Raises:
        None

    Side Effects:
        Reads from input_file
        Writes to output_file
        Writes to stats_file
        Prints errors to stderr
        Writes to logs

    Idempotent:
        True
    """
    xs = [int(x) for x in input_file.read().splitlines()]
    raised_errors = []
    logger.info("Beginning sorting")

    try:
        running_stats = json.load(stats_file)
        if not isinstance(running_stats, list):
            running_stats = []
        running_stats.append(context.__dict__)
        json.dump(running_stats, stats_file)
        output_file.write(str(xs))

    except (ValueError, IOError) as err:
        raised_errors.append(
            f"ERROR: {input_file.name}: {err}")
    if raised_errors:
        logger.warning("Errors raised")
        print_errors(raised_errors)


def print_errors(errors: list[str]) -> None:
    """Prints error information to stderr

    Error information includes preamble with usage information
    and each of the error messages provided in arg 'errors'.

    Args:
        errors: list[str] where each element contains details
        of the error that occurred, e.g. file, line number, message

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
        f"""\nWARNING: {len(errors)} errors found during sorting!""",
        "-"*80,
    ]
    for msg in error_preamble:
        print(msg, file=stderr)

    for error in errors:
        logger.error(error)
        print(error, file=stderr)
