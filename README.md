# doc-filler

A simple script to fill in word doc.

## Set up 
1. Install python3 - quick beginner guide [here](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Change  `template.docx` and `input_file.xlsx` files inside the input folder accordingly to your needs - [more about format of the two file here](## Format input files)
3. Run the following `pip install -r requirements.txt` to install all python libraries required 
4. Run `python main.py` to get the final result 

## Format input file
### Template
You can check the official documentation of *python-docx-template* library used in the project [here](https://docxtpl.readthedocs.io/en/latest/). 

### Input file
The `input_file.xlsx` need to have a column for each variable present in the `template.docx` file. 
The column name must match the variable name chose in the `template.docx` and the variable value must be placed in the 2nd row.
