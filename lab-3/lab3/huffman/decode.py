from lab3.huffman.encode import build_huffman_encoding_tree
from lab3.huffman.tree import Node

from typing import List


def decompress(s: str, frequency_table: List|Node) -> str:
    # Implementation adapted from ZyBook
    if isinstance(frequency_table, list):
        root = build_huffman_encoding_tree(freq_table=frequency_table)
    elif isinstance(frequency_table, Node):
        root = frequency_table
    else:
        raise ValueError("Was not able to process the frequency table during decompression")
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
