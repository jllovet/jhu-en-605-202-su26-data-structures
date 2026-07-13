from typing import Generator

def _pre2post(expression: str, index:int) -> Generator[str]:
    while index < len(expression):
        yield expression[index]
        index += 1

a =_pre2post("abc",0)

while True:
    try:
        print(next(a))
    except StopIteration:
        break
