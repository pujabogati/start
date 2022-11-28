from setuptools import setup

setup(
  name='FakeSnowflakes',

  version='0.0.1',

  author='Bogo',

  author_email='puja.bogati@gmail.com',

  packages=['snowhite'],

  license='LICENSE',

  description='Snowfall experience with different colours',

  long_description=open('README.md').read(),

  install_requires=["numpy==1.21.6","turtles==1.0.0","pygetwindow==0.0.9","pyautogui==0.9.53"],
)