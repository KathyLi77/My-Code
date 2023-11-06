#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:19:20 2022

@author: lijiaqi
"""

import re
import pyperclip

#These recognize the student id pattern and sibling number pattern

idRegex=re.compile(r'A\d-\d\d\d\d')
siblingsRegex=re.compile(r'#\d\d')

#Pasting the text in clipboard

textString = str(pyperclip.paste())

# Collecting items that match the pattern and add them into lists

moStudentId = idRegex.findall(textString)
moSiblingsNumber = siblingsRegex.findall(textString)






