from setuptools import setup

setup(
   name='shepard',
   version='0.1',
   description='handy tools for NWN EE modding designed for the Echoes of War persistent world',
   packages=['shepard'],
   include_package_data=True,
   install_requires=[
      'click'
   ],
   entry_points={
      'console_scripts': [
         'shepard = shepard.main:cli',
      ],
   },
)