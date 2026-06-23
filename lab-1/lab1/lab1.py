from sys import stderr
from typing import TextIO
import lab1.convert.converter as converter


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """Reads -> converts -> writes prefix expressions

    Reads prefix expressions from an input file, converts them into
    postfix expressions directly, and writes them to an output file.
    This is the logical entrypoint to the program when called as a module,
    where __main__ will call it with files passed from the command line.

    Args:
        input_file: TextIO is an opened text file set to read mode, and it
        contains prefix expressions to convert
        output_file: TextIO is an opened text file set to write mode, and it
        is the file the postfix expressions are written to

    Returns:
        None

    Raises:
        None

    Side Effects:
        Reads from input_file
        Writes to output_file
        Prints errors to stderr

    Idempotent:
        True
    """
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
        f"""WARNING: {len(errors)} errors found during conversion
WARNING: Invalid expressions not written to output file\n
Check expressions to ensure the are well formed and only use allowed symbols.\n
Note: whitespace is not allowed. Expressions with whitespace will be rejected.\n
Allowed symbols: ABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/$()\n
Example valid expressions:
\t(base case):\t'A'\t-> '{converter.pre2post('A')}'
\t(single op):\t'+AB'\t-> '{converter.pre2post('+AB')}'
\t(more ops):\t'-+ABC'\t-> '{converter.pre2post('-+ABC')}'""",
        "-"*80,
        "ERRORS:"
    ]
    for msg in error_preamble:
        print(msg, file=stderr)

    for error in errors:
        print(error, file=stderr)
