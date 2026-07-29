from lab3.huffman.encoding.encode import build_huffman_encoding_tree
from typing import List


def decompress(s: str, frequency_table: List) -> str:
    # Implementation adapted from ZyBook
    root = build_huffman_encoding_tree(freq_table=frequency_table)
    node = root
    buf = []
    for b in s:
        if node is None:
            break
        if str(b) == "0":
            node = node.left
        else:
            node = node.right
        if node.left is None and node.right is None:  # type: ignore
            buf.append(node.data.characters)  # type: ignore
            node = root
    res = "".join(buf)
    return res
