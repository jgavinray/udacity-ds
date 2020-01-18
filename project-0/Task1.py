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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create a list that will store unique telephone numbers
unique_numbers = set()

# There are two telephone numbers in each element of the lists,
# we will check to see if a number is found within the unique_numbers
# list and append if the number is not found.
# O(2n)
for call in calls:
	# Check the first telephone number at this list location
	unique_numbers.add(call[0])
	# Check the second telephone number at this list location
	unique_numbers.add(call[1])
# O(2n)
for text in texts:
	# Check the first telephone number at this list location
	unique_numbers.add(text[0])
	# Check the second telephone number at this list location
	unique_numbers.add(text[1])
# O(2n ^ 2 + 1)
print("There are {0} different telephone numbers in the records.".format(len(unique_numbers)))

