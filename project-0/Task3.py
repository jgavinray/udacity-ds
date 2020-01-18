"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

class Calls:
	def __init__(self):
		self.to_codes = set()

		self.bangalore_fixed_callers = 0
		self.bangalore_fixed_received = 0

	def start_sort(self, calls_list):
		# O(3n)
		for call in calls_list:
			if self._is_bangalore_fixed_line(call[0]):
				self.bangalore_fixed_callers += 1
				if call[1].startswith('(0'):
					self.to_codes.add(self._get_fixed_line_code_integer(call[1]))
					if self._is_bangalore_fixed_line(call[1]):
						self.bangalore_fixed_received = self.bangalore_fixed_received + 1
			
				result = self._get_mobile_number_prefix(call)
				if result:
					self.to_codes.add(result)

	def _is_bangalore_fixed_line(self, call):
		return call.startswith('(080)')

	def _get_fixed_line_code_integer(self, call):
		# O(1)
		if call.startswith('(0'):
			code = call.split(')', 1)[0]
			code = code[1:]
			return code

	def _get_mobile_number_prefix(self, call):
		# O(1)
		if call[1].startswith('7') or call[1].startswith('8') or call[1].startswith('9') and ' ' in call[1]:
				string = call[1]
				return string[:4]

	def print_codes(self):
		# O(n + 1)
		print("The numbers called by people in Bangalore have codes:")
		for code in sorted(self.to_codes):
			print(code)
	def _calc_percentage(self):
        # O(1)
		math_is_hard = (float(self.bangalore_fixed_received) / float(self.bangalore_fixed_callers)) * 100
		return math_is_hard

	def print_percentage(self):
		# O(1)
		result = self._calc_percentage()
		print("%.2f percent of calls from fixed lines in Bangalore are calls" \
				" to other fixed lines in Bangalore." % result)

c = Calls()
c.start_sort(calls)
c.print_codes()
c.print_percentage()