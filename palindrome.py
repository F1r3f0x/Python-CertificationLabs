"""
    Palindrome
    @f1r3f0x
"""

IS_PALINDROME = 'It\'s a palindrome'
NOT_PALINDROME = 'It\'s not a palindrome'


def is_palindrome(text: str) -> str:
    if len(text) == 0:  # assume that an empty string isn't a palindrome;
        return NOT_PALINDROME
    
    # treat upper- and lower-case letters as equal;
    # spaces are not taken into account during the check - treat them as non-existent;
    processed_text = text.strip().lower().split()
    
    processed_text = ''.join(processed_text)
    
    if processed_text == processed_text[::-1]:
        return IS_PALINDROME
    else:
        return NOT_PALINDROME


if __name__ == '__main__':
    assert is_palindrome('Ten animals I slam in a net') == IS_PALINDROME   
    assert is_palindrome('Eleven animals I slam in a net') == NOT_PALINDROME
    
    print(is_palindrome(input('Enter some text: ')))