from morse_code_converter import code_text, decode_text
import winsound
import time

frequency = 2000  # 2000Hz
duration_dot = 200  # 200ms
duration_dash = 600  # 600ms
duration_delay = 2  # 2s

def get_option():
    return input("--> To start encoder type 'C' <--\n"
                 "--> To start decoder type 'D' <--\n"
                 "--> To EXIT type anything else <--\n"
                 "Your option: ")

def get_output_type(input_text):
    return input(f"\nOriginal text: {input_text}\n"
                 "--> To get text output type 'T' <--\n"
                 "--> To get soud output type 'S' <--\n"
                 "--> To finish current translation type anything else <--\n"
                 "Your option: ")

def sound_output(converted_text):
    for c in converted_text:
        if c == '.':
            winsound.Beep(frequency, duration_dot)
        elif c == '-':
            winsound.Beep(frequency, duration_dash)
        elif c == ' ':
            time.sleep(duration_delay)

direction = get_option()

while direction in ['C', 'D']:
    input_text = input("Type text for conversion: ")
    if direction == 'C':
        try:
            converted_text = code_text(input_text)
        except ValueError as error:
            print(error)
        else:
            output_type = get_output_type(input_text)

            while output_type in ['T', 'S']:
                if output_type == 'T':
                    print(f"Coded text: {converted_text}")
                elif output_type == 'S':
                    sound_output(converted_text)
                input("Type Enter to continue...")
                output_type = get_output_type(input_text)

            print('\033c', end='')                
    else:
        try:
            text = decode_text(input_text)
        except ValueError as error:
            print(error)
        else:
            print(f"Decoded text: {text}")
    direction = get_option()
