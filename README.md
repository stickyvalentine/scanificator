## scanificator

If python 2.7 is installed and included in the Path, the file 'scanificator.py' can be run with out compiling. 



# Compile to .exe:

Install Python 2.7. Make sure to install it with the option to have Python in the Path. 

The module 'xlwt' is required for spreadsheet handling

Install py2exe for python 2.7.

Make sure that setup.py refers to the correct file name for the scanner program. In this case it is 'scanificator.py'

Make sure that setup.py and the scanner program are both in the same directory.

From that directory, run 'python setup.py py2exe'.

It will create 2 directories. 'Dist' is the compiled program.
