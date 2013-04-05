#!/usr/bin/python

from distutils.core import setup
setup(name='mips32',
      version='0.1',
      py_modules=['mips32'],
      description='A rudimentary MIPS32 assembler',
      scripts=['scripts/mips32-assemble'],
      author='John Trammell',
      author_email='johntrammell+pypi@gmail.com')
