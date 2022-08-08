#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """indent text"""
    if type(text) != str:
        raise TypeError('text must be a string')
    delimeters = ['.','?']
    sentence = (':' + '\n\n').join([i.strip(" ") for i in text.split(':')])
    sentence = ('.' + '\n\n').join([j.strip(" ") for j in sentence.split('.')])
    sentence = ('?' + '\n\n').join([k.strip(" ") for k in sentence.split('?')])
    print(sentence, end="")

if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")

