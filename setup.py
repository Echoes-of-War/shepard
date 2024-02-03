from setuptools import setup

setup(
   name='shepard',
   version='0.1',
   description='handy tools for NWN EE modding designed for the Echoes of War persistent world',
   author='Siobhan Buck',
   author_email='siobhan.buck@gmail.com',
   packages=['shepard'],  #same as name
   install_requires=['pyyaml'], #external packages as dependencies
)