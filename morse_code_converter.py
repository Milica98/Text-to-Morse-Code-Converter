
from letter_to_morse_mapping import morse_mapper

letter_code_dict = {letter_code_dict['letter']: letter_code_dict['morse']
                    for letter_code_dict in morse_mapper}

code_letter_dict = {letter_code_dict['morse']: letter_code_dict['letter']
                    for letter_code_dict in morse_mapper}


def get_coded_letter(letter):
    try:
        coded_letter = letter_code_dict[letter.upper()]
    except KeyError:
        raise ValueError(f"{letter} cannot be coded")
    else:
        return coded_letter


def code_text(text):
    try:
        converted_text = ' '.join([get_coded_letter(letter)
                                   for letter in text])
    except ValueError as error:
        raise error
    else:
        return converted_text


def get_decoded_letter(letter_code):
    try:
        letter = code_letter_dict[letter_code.upper()]
    except KeyError:
        raise ValueError(f"{letter_code} cannot be decoded")
    else:
        return letter


def decode_text(coded_text):
    coded_text_array = coded_text.split(' ')
    try:
        text = ''.join([get_decoded_letter(coded_letter)
                        for coded_letter in coded_text_array])
    except ValueError as error:
        raise error
    else:
        return text
