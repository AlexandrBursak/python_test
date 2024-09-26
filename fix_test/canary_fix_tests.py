import re
import os

# Example of files with tests:
"""
consistency-tests.test_consistency.test_consistency[2022-01-25T21:34[50]]
consistency-tests.test_consistency.test_consistency[2022-01-25T21:34[68]]
consistency-tests.test_consistency.test_consistency[2022-02-02T14:58[50]]
"""

def get_matches(line):
	regex = r".*\[([\d]{4}-[\d]{2}-[\d]{2}T[\d]{2}:[\d]{2})\[([\d]{2})\]\]$"

	for match in re.finditer(regex, line):
		return match.group(1), match.group(2)

def get_broken_test():
	count = 0
	tests = []
	file_with_tests = "list_of_test.txt"
	file = open(file_with_tests, 'r')
	lines = file.readlines()

	tests = [tuple(get_matches(line)) for line in lines]
	return tests

def run_fix_script(data):
	os.system("tox -e score -- --rescore --generation-name '{data[0]}' --generation-items {data[1]}")

for data in get_broken_test():
	run_fix_script(data)
