from setuptools import setup

setup(
   name='PyHelium',
   version='0.1.0',
   author='Aimé Risson',
   author_email='aime.risson.1@gmail.com',
   packages=['pyHelium'],

   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description="A simple python package to access Helium network's APi",
   long_description=open('README.md').read(),
   install_requires=[
       "requests",
   ],
)