"""
    Dynamic caesar Cypher
    @f1r3f0x
"""

def caesar_encode(text: str, shift_value: int):
    
    assert len(text) > 0
    assert 1 <= shift_value <= 25
    
    cypher = ''
    for char in text:
        if not char.isalpha():
            cypher += char
            continue
        
        # Shift Letter
        # A(65) - Z(90)
        # a(97) - z(122) 
        char_value = ord(char)
        shifted_value = char_value + shift_value
        
        if (
            (65 <= char_value <= 90 and shifted_value > 90) or
            (97 <= char_value <= 122 and shifted_value > 122)
        ):
            shifted_value -= 26
        
        shifted_char = chr(shifted_value)
        cypher += shifted_char
    
    return cypher
    

if __name__ == '__main__':
    
    cypher = caesar_encode('abcxyzABCxyz', 2)
    print(cypher)
    assert cypher == 'cdezabCDEzab'
    
    cypher = caesar_encode('The die is cast', 25)
    print(cypher)
    assert cypher == 'Sgd chd hr bzrs'
