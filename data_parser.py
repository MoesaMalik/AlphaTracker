import csv
from collections import defaultdict

	# defaultdict saves you from having to initialize lists for every header

def parse_csv(filename):
	value_dict = defaultdict(list)

	with open(filename, mode='r') as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			for header, value in row.items():
				value_dict[header].append(value)

	infile.close()
	return value_dict

if __name__ == '__main__':

	print(parse_csv("closed_trades.csv"))


