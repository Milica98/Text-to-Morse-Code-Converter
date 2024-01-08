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
                 "--> To get soud output type 'L' <--\n"
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

def cursor_off():
    print('\033[?25l', end="", flush=True)

def cursor_on():
    print('\033[?25h', end="", flush=True)

def delete_characters(len):
    while len > 0:
        print('\b ', end='')
        print('\b', end='')
        len -= 1
    print('', end='', flush=True)

def light_on(time_duration):
    print('\u2588' * 5, end='', flush=True)
    time.sleep(time_duration)

    delete_characters(5)
    time.sleep(0.5)

def light_output(converted_text):
    cursor_off()
    time.sleep(1)
    for c in converted_text:
        if c == '.':
            light_on(duration_dot / 1000.0)
        elif c == '-':
            light_on(duration_dash / 1000.0)
        elif c == ' ':
            time.sleep(duration_delay)
    time.sleep(1)
    cursor_on()

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

            while output_type in ['T', 'S', 'L']:
                if output_type == 'T':
                    print(f"Coded text: {converted_text}")
                elif output_type == 'S':
                    sound_output(converted_text)
                elif output_type == 'L':
                    light_output(converted_text)
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
