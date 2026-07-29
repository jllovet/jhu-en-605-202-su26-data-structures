from typing import List


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
