from os.path import exists
from setuptools import setup

setup(name='classtoolz',
      version='0.1',
      description='Class utilities',
      url='http://github.com/mrocklin/classtoolz',
      author='Matthew Rocklin',
      author_email='mrocklin@gmail.com',
      license='BSD',
      packages=['classtoolz'],
      long_description=open('README.md').read() if exists("README.md") else "",
      zip_safe=False)
