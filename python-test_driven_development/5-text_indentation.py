#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """indent text"""
    if type(text) != str:
        raise TypeError('text must be a string')
    sentence = (':' + '\n\n').join([i.strip(" ") for i in text.split(':')])
    sentence = ('.' + '\n\n').join([j.strip(" ") for j in sentence.split('.')])
    sentence = ('?' + '\n\n').join([k.strip(" ") for k in sentence.split('?')])
    print(sentence, end="")
