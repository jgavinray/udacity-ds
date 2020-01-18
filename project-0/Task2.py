"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# In the calls data set - assuming the data is organized in the following manner:
# <caller>,<recipient>,<date/time>,<call length in seconds>

class Calls:
	def __init__(self):
		self.unique_numbers = {}
		self.number_longest_called = None

	def print_longest_call(self, calls_list):
		"""
        	:type calls_list: list
        	:param calls_list: List rendered from csv file.
    	"""
		# O(1)
		self._iterate_through_calls(calls_list)

		print("{0} spent the longest time, {1} seconds on the phone during\nSeptember 2016."\
			.format(self.number_longest_called, self.unique_numbers[self.number_longest_called]))

	def _iterate_through_calls(self, calls_list):
		"""
        	:type calls_list: list
        	:param calls_list: List rendered from csv file.
    	"""
		# O(n + 2n)
		for call in calls_list:
			# Each of the first elements of the calls list are phone numbers.
			elements = range(2)
			for element in elements:
				self._update_unique_numbers(call, element)
				self._update_number_longest_called(call, element)

	def _update_unique_numbers(self, call, element):
		"""
        	:type call: list
        	:param call: List that contains telephone numbers in the first two elements
        	:type element: int
        	:param element: Which element of list to check
    	"""
		# If the key does not exist - create it and set its initial
		# value.
		# The average case of this is O(n^2) as we are iterating through two lists.
		if call[element] not in self.unique_numbers.keys():
			self.unique_numbers[call[element]] = int(call[3])
		# If the key DOES exist then we want to update it:
		elif call[element] in self.unique_numbers.keys():
			current_time_spent_on_calls = self.unique_numbers[call[element]]
			# Add the new value to the existing value:
			self.unique_numbers[call[element]] = current_time_spent_on_calls + int(call[3])

	def _update_number_longest_called(self, call, element):
		"""
        	:type call: list
        	:param call: List that contains telephone numbers in the first two elements
        	:type element: int
        	:param element: Which element of list to check
        """
        #O(1)
        # Base case - on first pass make sure that the number_longest_call is set
		if self.number_longest_called is None:
			self.number_longest_called = call[element]

		# Check to see if the value of the current unique number is greater than 
		# the number with the longest call.
		if self.unique_numbers[call[element]] > self.unique_numbers[self.number_longest_called]:
			self.number_longest_called = call[element]

c = Calls()
c.print_longest_call(calls)

# ~ 25 hours is a long time
