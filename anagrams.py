""""
    Anagrams
    @f1f3f0x
"""

from collections import defaultdict

ARE_ANAGRAMS = 'Anagrams'
NOT_ANAGRAMS = 'Not Anagrams'


def are_anagrams(words: [str]) -> str:

    assert len(words) == 2, 'Should be only two words'
    assert len(words[0]) == len(words[1]), 'The words should be of the same length'

    word_1 = words[0].lower()
    word_2 = words[1].lower()

    # Diffing the qty of each char for each string to know if they are anagrams
    counts = defaultdict(int)
    for i in range(len(words[0])):
        char_1 = word_1[i]
        char_2 = word_2[i]
        counts[char_1] += 1
        counts[char_2] -= 1

    for q in counts.values():
        if q > 0:
            return NOT_ANAGRAMS

    return ARE_ANAGRAMS


if __name__ == '__main__':
    assert are_anagrams(['Listen', 'Silent']) == ARE_ANAGRAMS
    assert are_anagrams(['modern', 'norman']) == NOT_ANAGRAMS

    print(are_anagrams(input('Type two words: ').split()))
