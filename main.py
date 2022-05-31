import csv
import os
import re
import sys
from docxtpl import DocxTemplate


def render_doc(fpath, context, fname):
	template = DocxTemplate(fpath)
	template.render(context)
	template.save(fname)


def get_name_list(csv_path, dir_path='../'):
	with open(dir_path + csv_path, newline='', encoding='utf-8-sig') as f:
		content = csv.DictReader(f, dialect='excel')
		name_list = []
		for row in content:
			name_list.append(row['name'])
	return name_list


def get_docx_listdir(path='..'):
	fname_list = os.listdir(path)
	return [fname for fname in fname_list if re.match(".*docx$", fname)]


def get_csv_listdir(path='..'):
	fname_list = os.listdir(path)
	return [fname for fname in fname_list if re.match(".*csv$", fname)]

def get_doc_listdir(doc_type, path='..')
	fname_list = os.listdir(path)
	return [fname for fname in fname_list if re.match(doc_type, fname)]

def fill_in_doc(entity, suffix, res_dir='./certificates/', dir_path='../'):
	template_path = get_docx_listdir()[0]
	csv_path = get_csv_listdir()[0]
	for name in get_name_list(csv_path):
		context = {'name': name}
		fname = 'certificado_{}_{}_{}.docx'.format(name, entity, suffix)
		render_doc(dir_path + template_path, context, res_dir + fname)


def main():
    xlsx_path = get_doc_listdir(".*xlsx$")[0]
    template_path = get_doclistdir(".*docx")[0]


if __name__ == '__main__':
	if (len(sys.argv) == 3):
		entity = sys.argv[1]
		suffix = sys.argv[2]
		fill_in_doc(entity, suffix)
	else:
		print('Launch with 2 arguments: entity name and suffix')
	
