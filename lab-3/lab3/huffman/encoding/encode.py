from typing import List, Dict, Tuple
from lab3.huffman.encoding.tree import MinHeap, Node
from lab3.huffman.encoding.normalize import normalize

DEFAULT_TABLE = ["A - 19", "B - 16", "C - 17", "D - 11", "E - 42", "F - 12", "G - 14", "H - 17", "I - 16", "J - 5", "K - 10", "L - 20",
                 "M - 19", "N - 24", "O - 18", "P - 13", "Q - 1", "R - 25", "S - 35", "T - 25", "U - 15", "V - 5", "W - 21", "X - 2", "Y - 8", "Z - 3"]


class EncodingData:
    """Representation of data for encoding. Contains characters and score.
    Comparison prioritizes score, then length, then alphabetic order.
    """

    def __init__(self, characters: str, score: int):
        self.characters = characters
        self.score = score

    def __repr__(self) -> str:
        return f"{self.characters} {self.score}"

    def __str__(self) -> str:
        return f"{self.characters} {self.score}"

    def __eq__(self, other: EncodingData) -> bool:
        same_score = self.score == other.score
        same_characters = self.characters == other.characters
        return same_score and same_characters

    def __lt__(self, other):
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return True
        if self.score > other.score:
            return False
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return True
        if len(self.characters) > len(other.characters):
            return False
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters < other.characters

    def __gt__(self, other: EncodingData) -> bool:
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return False
        if self.score > other.score:
            return True
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return False
        if len(self.characters) > len(other.characters):
            return True
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters > other.characters

    def __le__(self, other):
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score <= other.score:
            return True
        if self.score > other.score:
            return False
        # implies that self.score == other.score
        # Length
        if len(self.characters) <= len(other.characters):
            return True
        if len(self.characters) > len(other.characters):
            return False
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters <= other.characters

    def __ge__(self, other: EncodingData) -> bool:
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return False
        if self.score >= other.score:
            return True
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return False
        if len(self.characters) >= len(other.characters):
            return True
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters >= other.characters


def frequency_to_encoding_data(frequency_table: List[str]) -> List[EncodingData]:
    encoding_data = []
    for i, freq in enumerate(frequency_table):
        stripped_line = freq.strip()
        if stripped_line == "":
            continue
        parts = stripped_line.split(" - ")
        if len(parts) != 2:
            raise ValueError(
                f"The frequency table is invalid in row {i}: '{freq}' should be in the form 'A - 1'")
        char = parts[0]
        try:
            score = int(parts[1])
        except TypeError:
            raise ValueError(
                f"The frequency table is invalid in row {i}: In '{freq}' could not parse int. Should be in the form 'A - 1'")
        encoding_data.append(EncodingData(characters=char, score=score))
    return encoding_data


def build_huffman_encoding_tree(freq_table=DEFAULT_TABLE) -> Node:
    # Description of algorithm quoted from ZyBook
    # A Huffman tree can be built from a character frequency table.
    # First, each (character, frequency) pair from the table becomes a leaf node.
    # Next, all leaf nodes are inserted into a priority queue.
    # Then a loop does the following while the priority queue's length is at least two:
    # Dequeue the two nodes with the two lowest frequencies
    # Make an internal parent node with the two dequeued nodes as children
    # Insert the parent node into the priority queue
    freqs = frequency_to_encoding_data(freq_table)
    h = MinHeap()
    for f in freqs:
        h.enqueue(Node(data=f, left=None, right=None, parent=None))

    while h.length() >= 2:
        a = h.dequeue()  # type: ignore
        b = h.dequeue()  # type: ignore
        characters = a.data.characters + b.data.characters  # type: ignore
        score = a.data.score + b.data.score  # type: ignore
        c = Node(
            data=EncodingData(characters=characters, score=score),
            left=a,
            right=b)
        h.enqueue(c)

    s = h.dequeue()
    print(s)
    if s is None:
        return Node()
    else:
        return s


def get_huffman_codes_from_tree(node: Node, prefix="", codes=dict()) -> Dict:
    # Implementation adapted from ZyBook
    if node.left is None and node.right is None:
        codes[node.data.characters] = prefix
    else:
        _ = get_huffman_codes_from_tree(
            node.left, prefix=f"{prefix}0", codes=codes)  # type: ignore
        _ = get_huffman_codes_from_tree(
            node.right, prefix=f"{prefix}1", codes=codes)  # type: ignore
    return codes


def compress(s: str, frequency_table: List) -> Tuple[str, Node, Dict]:
    # Implementation adapted from ZyBook
    h = build_huffman_encoding_tree(freq_table=frequency_table)
    codes = get_huffman_codes_from_tree(node=h, prefix="", codes=dict())
    normal = normalize(s)
    buf = [codes[c] for c in normal]
    res = "".join(buf)
    return res, h, codes

