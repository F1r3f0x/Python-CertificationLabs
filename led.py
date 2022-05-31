'''
    PE-2 Lab: A LED Display
    @f1r3f0x
'''
led_numbers = [
    '#### ## ## ####',  # 0
    '  #  #  #  #  #',  # 1
    '###  #####  ###',  # 2
    '###  ####  ####',  # 3
    '# ## ####  #  #',  # 4
    '####  ###  ####',  # 5
    '####  #### ####',  # 6
    '###  #  #  #  #',  # 7
    '#### ##### ####',  # 8
    '#### ####  ####'   # 9
]


def print_number(number: int) -> None:
    number_str = str(number)
    numbers_to_print = []
    
    # Get Numbers
    for num in number_str:
        numbers_to_print.append(led_numbers[int(num)])
    
    # Print Lines
    for y in range(5):
        line_chars = []
        for idx, num in enumerate(numbers_to_print):
            line_chars.append(numbers_to_print[idx][y*3:y*3+3])
            line_chars.append(' ')
        print(''.join(line_chars))


if __name__ == '__main__':
    print_number(1234567890)   