# define2html

The program takes a define.xml as an input and uses the define2-1.xsl stylesheet to generate a define.html output.

## Usage

Example command-line using all 3 parameters:
```
python3 define2html.py -d ./define.xml -o ./define.html -x ./define2-1.xsl
```

By default, the program will look for a define.xml file and define2-1.xsl stylesheet in the same directory as 
define2html.py. The output defaults to writing a define.html in the current directory. The following command-line uses
all 3 default parameters.
```
python3 define2html.py
```

## Future

Future plans include transforming this small program into a Python library to use in other projects. Other improvements
include adding error handling.