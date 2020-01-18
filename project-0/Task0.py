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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Assuming that each of the texts in CSV list has the following composition:
# incoming number, answering number, date/time, seconds
print("First record of text, {0} texts {1} at time {2}".format(texts[0][0], \
	texts[0][1], texts[0][2]))

# Assuming that each of the calls in CSV list has the following composition:
# incoming number, answering number, date/time, seconds
number_of_calls = len(calls)
# List starts at 0 to minus 1 from the total list length
number_of_calls = number_of_calls - 1
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds" \
		.format(calls[number_of_calls][0], calls[number_of_calls][1], \
		calls[number_of_calls][2],calls[number_of_calls][3]))
# O(4)
