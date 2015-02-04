import fileinput
import re

for line in fileinput.input():
    match = re.search('^(.*)\s+(20\d\d)-(\d\d)-(\d\d)\s+(\d+\.?\d*)$', line)
    
    if match:
        fields = [
            match.group(2),  # year
            match.group(3),  # month
            match.group(4),  # day
            match.group(1),  # site
            match.group(5)   # value
        ]
        
        print fields
    else:
        print "Line {} did not match!".format(fileinput.lineno())
