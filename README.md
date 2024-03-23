# zip_flattener
A simple python program taking a zip file as input and generating one file containing the complete zip tree as well as for each contained file; the full name of the file and its contents.

## Test it
Use the example provided.
In main.py, you'll see that the script will look for a file named `my_test.zip` (variable zip_path). 
It contains a dummy java project.
The script will then extract that zip file in a directory called `extracted` (variable extract_to).
Finally, in output.txt, the script will generate a project tree and for each file contained:
- the name of the file
- the content of the file

## Customize
To make this script your own, simply paste your zip file at the root of the project, change the variable zip_path in the main.py file and execute the script:

> python3 main.py

That's it!

Enjoy

~ Memento