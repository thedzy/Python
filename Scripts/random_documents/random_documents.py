#!/usr/bin/env python3

"""
Script:	random_documents.py
Date:	2018-09-30

Platform: MacOS

Description:
Creates a random text (English language like) document.
With no parameters, it outputs to screen
With a file specified, it will output to file

"""
__author__      = 'thedzy'
__copyright__   = 'Copyright 2018, thedzy'
__license__     = 'GPL'
__version__     = '1.0'
__maintainer__  = 'thedzy'
__email__       = 'thedzy@hotmail.com'
__status__      = 'Developer'

import os
import sys
from random import *


def main():
    if len(sys.argv) == 1:
        print(document())

    # For file arguments
    for arg in range(1, len(sys.argv)):
        try:
            # Get filename
            filename = str(sys.argv[arg])

            # Check for txt extension
            extension = os.path.splitext(filename)[1][1:]
            if extension != 'txt':
                filename += '.txt'

            print('Writeing out to: ' + filename)
            file = open(filename, 'w')
        except OSError as error:
            print('OS error: {0}'.format(error))
            sys.exit()

        file.write(document())
        file.close()


def word(capital=False):
    """
    Create a pseudo english word
    :param capital: (Bool) Use captial letter
    :return: (String) word
    """
    fletters = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'gw', 'ph', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']
    cletters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'z', 'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'gh', 'gn', 'ph', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']
    vletters = ['a', 'e', 'i', 'o', 'u', 'ai', 'au', 'ay', 'ea', 'ee', 'ei', 'eu', 'ey', 'ie', 'oi', 'oo', 'ou', 'oy', 'eau', 'y']
    yletters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ch', 'ph', 'sh', 'sk', 'sp', 'st', 'th']
    zletters = ['a', 'e', 'i', 'o', 'u', 'ai', 'au', 'ay', 'ea', 'ee', 'eu', 'ey', 'ie', 'oi', 'oo', 'ou', 'oy', 'eau', 'y']

    wordlen = randint(0, 5)

    if wordlen == 0:
        word = sample(vletters, 1)[0]
    else:
        word = sample(fletters, 1)[0]

        for i in range(wordlen):
            if i % 2 == 0:
                word += sample(vletters, 1)[0]
            else:
                word += sample(cletters, 1)[0]

        if i % 2 == 0:
            word += sample(yletters, 1)[0]
        else:
            word += sample(zletters, 1)[0]

    if capital:
        word = word.title()

    return word


def sentance(words=0):
    """
    Create a pseudo english sentance
    :param words: (int) Number of words
    :return: (string) Sentance
    """
    punctuation = ['.', '.', '.', '.', '.', '.', '!', '?']
    quoted = False

    if words == 0:
        words = randint(2, 20)

    sentance = ''
    for i in range(words):
        if i == 0:
            sentance += word(True)
        else:
            # Chance of punctuation
            if i != words and randint(0, 100) == 0:
                sentance += '\'s'

            if randint(0, 10) == 0:
                sentance += ','
            elif randint(0, 100) == 0:
                    sentance += ';'
            elif randint(0, 200) == 0:
                    sentance += ':'

            # Space words or Hyphenate
            if randint(0, 200) == 0:
                sentance += '-'
            else:
                sentance += ' '

            # Chance of quote
            if randint(0, 100) == 0:
                quoted = True
                sentance += """
            sentance += word()

            # Close quotes out within x words
            if quoted and randint(0, 8) == 0:
                quoted = False
                sentance += """

    # Make sure quotes end
    if quoted:
        sentance += """

    return sentance + sample(punctuation, 1)[0] + ' '


def paragraph(sentances=0):
    """
    Create a pseudo english paragraph
    :param sentances: (Int) Number of sentances
    :return: (String) Paragraph
    """
    if sentances == 0:
        sentances = randint(5, 20)

    paragraph = ''
    for i in range(sentances):
        if i == 0:
            paragraph += sentance()
        else:
            paragraph += sentance()

    return paragraph + '\n\n'


def document(paragraphs=0):
    """
    Create a pseudo english document
    :param paragraphs: (Int) Number of paragraphs
    :return: (String) Document
    """
    if paragraphs == 0:
        paragraphs = randint(5, 20)

    document = ''
    for i in range(paragraphs):
        if i == 0:
            document += paragraph()
        else:
            document += paragraph()

    return document


if __name__ == '__main__':
    main()
