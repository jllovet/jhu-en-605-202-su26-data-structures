from lab1.stack import Stack
import lab1.parse.postfix as postfix
import lab1.parse.prefix as prefix
import lab1.parse.parser as parser


def pre2post(expression: str) -> str:
    if not prefix.is_valid(parser.parse(expression)):
        raise ValueError(f"{expression} is not a valid prefix expression")
    return expression
