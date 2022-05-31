"""
    My split
    @f1r3f0x
"""


def mysplit(strng):
    #
    # put your code here
    #
    split_list = []

    if len(strng) == 0:
        return split_list

    chars = []
    count = 0
    for character in strng:
        count += 1
        if character != ' ':
            chars.append(character)

        if len(chars) > 0 and (character == ' ' or count == len(strng)):
            split_list.append(''.join(chars))
            chars.clear()

    return split_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))