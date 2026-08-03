from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    word_count = {}
    for c in word:
        if c not in word_count:
            word_count[c] = 0
        word_count[c] += 1
    return word_count

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
