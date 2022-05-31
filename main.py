import csv
import os
import re
import sys
from docxtpl import DocxTemplate
import pandas as pd


path_input = 'input/'


def render_doc(fpath, context, fname):
	template = DocxTemplate(fpath)
	template.render(context)
	template.save(fname)


def get_doc_listdir(doc_type, path=path_input):
	fname_list = os.listdir(path)
	return [fname for fname in fname_list if re.match(doc_type, fname)]


def create_context(var_input_path):
    df = pd.read_excel(path_input + var_input_path)
    return df.to_dict(orient='records')[0]


def main(fname='res.docx'):
    template_path = get_doc_listdir(".*docx$")[0]
    var_input_path = get_doc_listdir(".*xlsx$")[0]
    context = create_context(var_input_path)
    render_doc(path_input + template_path, context, fname)
    print("Doc filled in ...")

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        fname = sys.argv[1]
        main(fname)
    else:
        main()
