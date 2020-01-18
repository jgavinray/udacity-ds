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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

class Telemarketer:
	def __init__(self):
		self.text_source_numbers = set()
		self.text_destination_numbers = set()

		self.calls_source_numbers = set()
		self.calls_destination_numbers = set()

		self.possible_telemarketers = []

	def create_list(self, calls_list, texts_list):
		"""
        	:type calls_list: list
        	:param calls_list: List that contains telephone numbers in the first two elements
        	:type texts_list: list
        	:param texts_list: List that contains text numbers in the first two elements
    	"""
		# The assumption for the text and call lists are that the first column is the number
		# where calls originate from, and the second column is the destination.

		# Split dataset up into 4 - source/destination for both text and calls
		# so comparisons can be done:
		# O(3)
		self._set_unique_text_numbers(texts_list)
		self._sort_unique_call_numbers(calls_list)

		# Check to see if any of the call source numbers have received any texts
		self._check_for_telemarketing_activity()

	def _set_unique_text_numbers(self, text_list):
		"""
		    :type texts_list: list
        	:param texts_list: List that contains text numbers in the first two elements
    	"""
		# Each iteration of this loop is O(4n) in worst case
		for text in text_list:
			# Get list of numbers that send texts:
			self.text_source_numbers.add(text[0])
			# Get list of numbers that receive texts:
			self.text_destination_numbers.add(text[1])

	def _sort_unique_call_numbers(self, calls_list):
		"""
        	:type calls_list: list
        	:param calls_list: List that contains telephone numbers in the first two elements
        """
		# Each iteration of this loop is O(4n) in worst case
		for call in calls_list:
			# Get list of numbers that send calls:
			self.calls_source_numbers.add(call[0])
			# Get list of numbers that receive calls:
			self.calls_destination_numbers.add(call[1])

	def _check_for_telemarketing_activity(self):
		# O(4n) as worst case scenario
		for number in self.calls_source_numbers:
			if self._has_sent_texts(number):
				continue
			if self._has_received_texts(number):
				continue
			if self._has_received_calls(number):
				continue
			if number not in self.possible_telemarketers:
				self.possible_telemarketers.append(number)

	def _has_sent_texts(self, number):
		"""
        	:type number: string
        	:param number: String to be checked against the text source numbers set
        """
		# O(1)
		if number in self.text_source_numbers:
			return True
		return False

	def _has_received_texts(self, number):
		"""
        	:type number: string
        	:param number: String to be checked against the text destination numbers set
        """
		# O(1)
		if number in self.text_destination_numbers:
			return True
		return False

	def _has_received_calls(self, number):
		"""
        	:type number: string
        	:param number: String to be checked against the text destination numbers set
        """
		# O(1)
		if number in self.calls_destination_numbers:
			return True
		return False

	def print_results(self):
		# O(1) best case
		if not self.possible_telemarketers:
			print("You really should try using the create_list method before calling this.")
			return

		# Don't know what the internal sort is on this method - runtime could vary.  Likely
		# an insertion sort because of the size of the lists
		self.possible_telemarketers.sort()

		# O(n+1) worst case
		print("These numbers could be telemarketers:")
		for number in self.possible_telemarketers:
			print(number)


t = Telemarketer()
t.create_list(calls, texts)
t.print_results()
