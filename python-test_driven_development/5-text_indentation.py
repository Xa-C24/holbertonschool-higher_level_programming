#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ignore_space = False

    for i in range(len(text)):
        
        if ignore_space and text[i] == ' ':
            continue
        ignore_space = False
        
       
        print(text[i], end="")

        
        if text[i] in ['.', '?', ':']:
            print("\n")
            ignore_space = True
            