#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# Code test for working with environment-
# variables with the os module on different
# systems

import os

fruit = os.getenv('fruit')
print(fruit)

