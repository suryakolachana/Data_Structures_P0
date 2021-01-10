"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

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
 - Mobile numbers have no parenheses, but have a space in the middle
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

codes_list = {}
count = 0
count2 = 0

for i in calls:
  if i[0].startswith("(080)"):
    if i[1].startswith("(0"):
         x = i[1].find('(') + 1
         y = i[1].find(')')
         codes_list[i[1][x:y]] = 0
    if i[1].startswith("7") or i[1].startswith("8") or i[1].startswith("9"):
      codes_list[i[1][0:4]] = 0

print("The numbers called by people in Bangalore have codes:")
for j in sorted(codes_list):
  print(j)

for k in calls:
  if k[0].startswith("(080)"):
      count2 = count2 +1
  if k[0].startswith("(080)") and k[1].startswith("(080)"):
      count = count + 1

calPercent = round((count/count2) * 100,2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(calPercent))
