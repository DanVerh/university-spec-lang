from .letters import *


def generateArt(text, size):
    rows = []
    for line in text.split('\n'):
        row = []
        for char in line:
            if char.isalpha() and size == "small":
                row.append(lowercase_letters[char])
            elif char.isalpha() and size == "big":
                row.append(uppercase_letters[char])
        rows.append(row)

    # Combine rows to create the final map
    map_lines = [''.join(chars) for chars in zip(*rows)]
    map_str = '\n'.join(map_lines)
    return map_str