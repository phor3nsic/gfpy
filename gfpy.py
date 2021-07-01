import re
import argparse
import json
import sys

def get_param(line):
	regex = re.compile("([\\w%]{0,})(?=\\=)")
	matchArray = regex.findall(line)
	parameters = []
	try:
		for x in matchArray:
			if x != "":
				x = x + "="
				parameters.append(x)
	except:
		pass

	return parameters

def compare_param(parameters, list_of_partteners):
	for param in parameters:
		if param in list_of_partteners:
			return True
		else:
			return False

def read_pattern(json_file):
	f = open(json_file)
	data = json.load(f)
	return data["patterns"]
	f.close()


def main():
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument("-f", "--file", help="File with params", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("-p","--patterns", help="GF-Patterns list", required=True)
	args = parser.parse_args()
	
	lines = args.file.readlines()

	for line in lines:
		line = line.replace("\n","")
		
		if compare_param(get_param(line),read_pattern(args.patterns)):
			print(f"{line}")
		

if __name__ == '__main__':
	main()


