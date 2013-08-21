#!/usr/bin/env python

from distutils.core import setup
import os

scripts = ['cheat']
if os.name == "nt":
    scripts.append('cheat.bat')


setup(name='cheat',
      version='1.0.1',
      description='Create and view interactive cheatsheets on the command-line',  # nopep8
      author='Chris Lane',
      author_email='chris@chris-allen-lane.com',
      url='https://github.com/chrisallenlane/cheat',
      packages=['cheatsheets'],
      package_data={'cheatsheets': [f for f in os.listdir('cheatsheets')
                                    if '.' not in f]},
      scripts=scripts
     )
