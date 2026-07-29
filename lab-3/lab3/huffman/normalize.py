from typing import List, Callable


def strip_non_alphabetic_char(s: str):
    """Returns a str with all non-alphabetic characters removed or empty str if s is not a str

    For example, Hello! -> Hello

    Args:
        s: str to be stripped to alphabetic characters

    Returns:
        str with all non-alphabetic characters removed

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(s, str):
        return ""
    return s if s.isalpha() else ""


def capitalize(s: str):
    """Returns the uppercase version of a string or empty str if s is not a str

    For example, c -> C, apple -> APPLE, άλφα -> ΆΛΦΑ

    Args:
        s: str to be capitalized

    Returns:
        Capitalized character or empty string

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(s, str):
        return ""
    return s.upper() if s else ""


def normalize(s: str, pipeline: List[Callable] = [strip_non_alphabetic_char, capitalize]):
    """Returns a normalized str after running each function in pipeline on each char

    Composes the functions in the pipeline with each other and applies to c from left to right
    For instance, if the pipeline is [f,g] and the str is s, then it returns g(f(s))

    Args:
        s: str to be normalized
        pipeline: list of functions to be composed in order to s

    Returns:
        Normalized string that has had pipeline functions applied to it

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    buf = []
    if not pipeline:
        return s
    if not s:
        return ""
    for character in s:
        normal_character = character
        for f in pipeline:
            if normal_character is not None:
                normal_character = f(normal_character)
            else:
                break
        if normal_character is not None:
            buf.append(normal_character)
        else:
            continue
    return "".join(buf)
