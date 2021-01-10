from setuptools import setup,find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='keyboard2mouse',
   version='0.0.6',
   description='A python program to map keyboard keys to mouse',
   long_description=long_description,
   license="GPL-3",
   author='Riccardo Isola',
   author_email='riky.isola@gmail.com',
   url="https://github.com/RikyIsola/Linux-Keyboard2Mouse",
   packages=find_packages(),
   install_requires=['pyautogui','pynput'],
   scripts=['keyboard2mouse']
)
