# doc-filler

A simple script to fill in word doc.

## Set up 
1. Install python3 - quick beginner guide [here](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Change  `template.docx` and `input_file.xlsx` files inside the input folder accordingly to your needs files.
You can upload your file as well - in this case they must follow the same formatting rules presented in the next section.
3. Run the following to set up a virtual env and to install all python libraries required 
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
deactivate
``` 

## Format input file
### Template
You can check the official documentation of *python-docx-template* library used in the project [here](https://docxtpl.readthedocs.io/en/latest/). 

### Input file
The `input_file.xlsx` need to have a column for each variable present in the `template.docx` file. 
The column name must match the variable name chose in the `template.docx` and the variable value must be placed in the 2nd row.

## Run the script
After completing the setting up steps, simply run the following in your terminal:
```
. venv/bin/activate
python main.py
deactivate
```
