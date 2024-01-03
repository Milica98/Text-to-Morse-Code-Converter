from morse_code_converter import code_text, decode_text


def get_option():
    return input("To start coder type 'C'; \nFor start decoder type 'D'; \nFor EXIT type anything else; \nYour "
                 "option: ")


direction = get_option()

while direction in ['C', 'D']:
    input_text = input("Type text for conversion: ")
    if direction == 'C':
        try:
            converted_text = code_text(input_text)
        except ValueError as error:
            print(error)
        else:
            print(f"Coded text: {converted_text}")
    else:
        try:
            text = decode_text(input_text)
        except ValueError as error:
            print(error)
        else:
            print(f"Decoded text: {text}")
    print("--------------------------------------------------------------------------------")
    direction = get_option()
