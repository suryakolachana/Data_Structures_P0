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
identified_telemarketers = set()
non_identified_telemarketers = set()

for i in calls:
    identified_telemarketers.add(i[0])
    non_identified_telemarketers.add(i[1])

for j in texts:
    non_identified_telemarketers.add(j[0])
    non_identified_telemarketers.add(j[1])

telemarketers = identified_telemarketers.difference(non_identified_telemarketers)

print("These numbers could be telemarketers: ")
for k in sorted(telemarketers):
    print(k)
