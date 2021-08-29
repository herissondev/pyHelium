from setuptools import setup

setup(
   name='PyHelium',
   version='0.1.0',
   author='Aimé Risson',
   author_email='aime.risson.1@gmail.com',
   packages=['pyHelium'],

   url='http://pypi.python.org/pypi/PackageName/',
   license='Mit License',
   description="A simple python package to access Helium network's APi",
   long_description=open('README.md').read(),
   long_description_content_type = "text/markdown",
   install_requires=[
       "requests",
   ],
)