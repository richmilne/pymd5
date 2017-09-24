"""Setup for pymd5 module and command-line script."""
from setuptools import setup

setup(name='pymd5',
      version='0.1',
      description=('Recursively calculate and display MD5 file hashes '
                   'for all files rooted in a directory.'),
      url='https://github.com/richmilne/pymd5',
      author='Richard Milne',
      author_email='richmilne@hotmail.com',
      license='MIT',
      packages=['pymd5'],
      entry_points={
          'console_scripts': ['pymd5=pymd5:_read_args']
      },
      include_package_data=True,
     )
